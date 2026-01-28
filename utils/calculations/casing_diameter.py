from database.data import SessionDep
from sqlalchemy import select, asc
from models.bit_standard import Bit
from models.casing_standard import StandardCasingDiameter
from fastapi import HTTPException
from models.well import Well
from models.well_constraction import Construction
from models.construction_diameter import ConstructionDiameter
from schemas.construction_diameter import Diameter



async def get_diameter(session: SessionDep, diameter: float, schema):
    stmt = (select(schema).where(schema.diameter >= diameter).
            order_by(asc(schema.diameter)).limit(1))
    result = await session.scalars(stmt)
    diameters = result.one_or_none()
    if diameters is None:
        raise HTTPException(status_code=404, detail="Suitable diameter not found.")
    return diameters


async def calculate_diameters(session: SessionDep, well_id: int, first_diameter: int) -> list[Diameter]:
    well = await session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found.")
    stmt = (select(Construction).
            where(Construction.well_id == well.id)
            .order_by(Construction.column_depth.desc()))
    result = await session.scalars(stmt)
    columns_db = result.all()
    if not columns_db:
        raise HTTPException(status_code=404, detail="Well not found")

    db_objects = []
    current_column_diameter = first_diameter
    casing_std = await get_diameter(session=session, diameter=current_column_diameter,
                              schema=StandardCasingDiameter)

    calc_bit = casing_std.coupling_diameter + casing_std.recommended_clearance
    bit_diameter = await get_diameter(session=session, diameter=calc_bit, schema=Bit)
    obj = ConstructionDiameter(
        well_id=well.id,
        column_depth=columns_db[0].column_depth,
        column_name=columns_db[0].column_name,
        column_diameter=first_diameter,
        bit_diameter=bit_diameter.diameter
    )
    session.add(obj)
    db_objects.append(obj)

    previous_bit_diameter = bit_diameter.diameter
    for column in columns_db[1:]:

        min_casing = previous_bit_diameter + 10
        casing_std = await get_diameter(session=session, diameter=min_casing, schema=StandardCasingDiameter)
        current_column_diameter = casing_std.diameter

        calc_bit = casing_std.coupling_diameter + casing_std.recommended_clearance
        current_bit = await get_diameter(session=session, diameter=calc_bit, schema=Bit)
        bit_diameter = current_bit.diameter

        obj = ConstructionDiameter(
            well_id=well.id,
            column_depth=column.column_depth,
            column_name=column.column_name,
            column_diameter=current_column_diameter,
            bit_diameter=bit_diameter
        )
        session.add(obj)
        db_objects.append(obj)
        previous_bit_diameter = bit_diameter
    await session.commit()
    for obj in db_objects:
        await session.refresh(obj)
    return [Diameter.model_validate(obj) for obj in db_objects]