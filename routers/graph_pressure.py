from fastapi import APIRouter, HTTPException

from utils.calculations.graph_pressure import calculate_parameters_all
from schemas.graph_pressure import HydraulicInput, HydraulicResult
from database.data import SessionDep
from models.graph_pressure import Info
from sqlalchemy import select, delete
from utils.graph.graph_pressure import build_graphic
from models.well import Well

router = APIRouter()

@router.post("/data",
             tags=["data"])
async def create_data(session: SessionDep, well_id: int,
                inputs: list[HydraulicInput]) -> list[HydraulicResult]:
    well = await session.get(Well, well_id)
    if not well:
        raise HTTPException(status_code=404, detail="Well not found")

    results = calculate_parameters_all(inputs)
    db_objects = []
    for result in results:
        db_obj = Info(
            well_id=well_id,
            pressure_mpa=result.pressure_mpa,
            depth_up_m=result.depth_up_m,
            depth_down_m=result.depth_down_m,
            anomaly_coefficient=result.anomaly_coefficient,
            fracturing_pressure_mpa=result.fracturing_pressure_mpa,
            fracturing_coefficient=result.fracturing_coefficient,
            fracturing_coefficient2=result.fracturing_coefficient2,
            mud_density=result.mud_density
            )
        session.add(db_obj)
        db_objects.append(db_obj)
    await session.commit()
    # for obj in db_objects:
    #     await session.refresh(obj)
    return [HydraulicResult.model_validate(db_obj) for db_obj in db_objects]


@router.get("/data{well_id}",
            tags=["data"],
            response_model=list[HydraulicResult])
async def read_data(session: SessionDep, well_id: int) -> list[HydraulicResult]:
    well = await session.get(Well, well_id)
    if not well:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = select(Info).where(Info.well_id == well_id)
    result = await session.scalars(stmt)
    parameters = result.all()
    if not parameters:
        raise HTTPException(status_code=404, detail="no data found")
    return [HydraulicResult.model_validate(parameter) for parameter in parameters]

@router.delete("/data/{well_id}",
               tags=["data"])
async def delete_data(session: SessionDep, well_id: int):
    well = await session.get(Well, well_id)
    if not well:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = delete(Info).where(Info.well_id == well_id)

    result = await session.execute(stmt)
    delete_count = result.rowcount
    if delete_count == 0:
        raise HTTPException(status_code=404, detail="no data found")
    await session.commit()
    return {"success": True,
            "deleted": delete_count}


@router.get("/graph",
            tags=["data"])
async def read_graph_data(session: SessionDep, well_id: int):
    return await build_graphic(session=session, well_id=well_id)
