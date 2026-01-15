from fastapi import HTTPException
from models.pressure import Pressure
from database.data import SessionDep
from sqlalchemy import select
from schemas.pressure import PressureCreate, PressureResponse, PressureUpdate


def create_pressure(session: SessionDep, pressure_data: PressureCreate):
    calculated_pressure = pressure_data.depth*pressure_data.density
    db_pressure = Pressure(
        density=pressure_data.density,
        depth=pressure_data.depth,
        pressure = calculated_pressure
    )
    session.add(db_pressure)
    session.commit()
    session.refresh(db_pressure)
    return PressureResponse.model_validate(db_pressure)

def get_pressures(session: SessionDep):
    stmt = select(Pressure)
    press = session.scalars(stmt).all()
    return [PressureResponse.model_validate(p) for p in press]

def get_pressure_by_id(session: SessionDep, id: int):
    press = session.get(Pressure, id)
    if not press:
        raise HTTPException(status_code=404, detail="Pressure not found")
    return PressureResponse.model_validate(press)

def get_pressure_by_depth(session: SessionDep, depth: int):
    stmt = select(Pressure).where(Pressure.depth == depth)
    press = session.scalars(stmt).one_or_none()
    if press is None:
        raise HTTPException(status_code=404, detail="Pressure not found")
    return PressureResponse.model_validate(press)

def update_pressure_id(session: SessionDep,
                    pressure_id: int,
                    update_data: PressureUpdate):
    press = session.get(Pressure, pressure_id)
    if not press:
        raise HTTPException(status_code=404, detail="Pressure not found")
    update_dict = update_data.model_dump(exclude_unset=True)

    for key, value in update_dict.items():
        setattr(press, key, value)
    if "depth" in update_dict or "density" in update_dict:
        press.pressure = press.depth*press.density
    session.commit()
    session.refresh(press)
    return PressureResponse.model_validate(press)


def remove_pressure_by_id(session: SessionDep, pressure_id: int):
    press = session.get(Pressure, pressure_id)
    if not press:
        raise HTTPException(status_code=404, detail="Pressure not found")
    session.delete(press)
    session.commit()
    return {"success": True}