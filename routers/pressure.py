# from fastapi import APIRouter
# from schemas.pressure import PressureResponse, PressureCreate, PressureUpdate
# from database.data import SessionDep
# from crud.pressure import (create_pressure, get_pressures,
#                            get_pressure_by_id, get_pressure_by_depth,
#                            update_pressure_id, remove_pressure_by_id)
#
# router = APIRouter()
#
# @router.post("/pressure",
#          response_model=PressureResponse)
# def pressure_create(session: SessionDep, pressure: PressureCreate):
#     return create_pressure(session=session, pressure_data=pressure)
#
# @router.get("/pressure",
#          response_model=list[PressureResponse])
# def read_pressures(session: SessionDep):
#     return get_pressures(session=session)
#
#
# @router.get("/pressure/{id}",
#          response_model=PressureResponse)
# def read_pressure_by_id(session: SessionDep, pressure_id: int):
#     return get_pressure_by_id(session=session, id=pressure_id)
#
# @router.get("/pressure_by_depth",
#          response_model=PressureResponse)
# def read_pressure_by_depth(session: SessionDep, pressure_depth: int):
#     return get_pressure_by_depth(session=session, depth=pressure_depth)
#
#
# @router.patch("/pressure/{id}",
#            response_model=PressureResponse)
# def update_pressure(session: SessionDep, pressure_id: int, update_data: PressureUpdate):
#     return update_pressure_id(session=session, pressure_id=pressure_id, update_data=update_data)
#
#
#
# @router.delete("/pressure/{id}")
# def delete_pressure_by_id(session: SessionDep, pressure_id: int):
#     return remove_pressure_by_id(session=session,
#                                  pressure_id=pressure_id)