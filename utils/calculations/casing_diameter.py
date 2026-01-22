from database.data import SessionDep
from sqlalchemy import select, asc
from models.bit_standard import Bit
from models.casing_standard import StandardCasingDiameter
from fastapi import HTTPException
from models.well import Well
from models.well_constraction import Construction
from models.construction_diameter import ConstructionDiameter
from schemas.construction_diameter import Diameter



def get_diameter(session: SessionDep, diameter: float, schema):
    stmt = (select(schema).where(schema.diameter >= diameter).
            order_by(asc(schema.diameter)).limit(1))
    result = session.scalars(stmt).one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail="Suitable diameter not found.")
    return result


def calculate_diameters(session: SessionDep, well_id: int, first_diameter: int) -> list[Diameter]:
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found.")
    stmt = (select(Construction).
            where(Construction.well_id == well.id)
            .order_by(Construction.column_depth.desc()))
    columns_db = session.scalars(stmt).all()
    if not columns_db:
        raise HTTPException(status_code=404, detail="Well not found")

    result = []
    current_column_diameter = first_diameter
    casing_std = get_diameter(session=session, diameter=current_column_diameter,
                              schema=StandardCasingDiameter)

    calc_bit = casing_std.coupling_diameter + casing_std.recommended_clearance
    bit_diameter = get_diameter(session=session, diameter=calc_bit, schema=Bit)
    db_obj = ConstructionDiameter(
        well_id=well.id,
        column_depth=columns_db[0].column_depth,
        column_name=columns_db[0].column_name,
        column_diameter=first_diameter,
        bit_diameter=bit_diameter.diameter
    )
    session.add(db_obj)
    result.append(Diameter.model_validate(db_obj))

    previous_bit_diameter = bit_diameter.diameter
    for column in columns_db[1:]:

        min_casing = previous_bit_diameter + 10
        casing_std = get_diameter(session=session, diameter=min_casing, schema=StandardCasingDiameter)
        current_column_diameter = casing_std.diameter

        calc_bit = casing_std.coupling_diameter + casing_std.recommended_clearance
        current_bit = get_diameter(session=session, diameter=calc_bit, schema=Bit)
        bit_diameter = current_bit.diameter

        db_obj = ConstructionDiameter(
            well_id=well.id,
            column_depth=column.column_depth,
            column_name=column.column_name,
            column_diameter=current_column_diameter,
            bit_diameter=bit_diameter
        )
        session.add(db_obj)
        result.append(Diameter.model_validate(db_obj))
        previous_bit_diameter = bit_diameter
    session.commit()
    return result