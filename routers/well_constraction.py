from fastapi import APIRouter, HTTPException

from models.well_constraction import Construction, CasingColumn
from schemas.well_constraction import ColumnResponse, ConductorInputParams, CasingDepth
from database.data import SessionDep
from models.well import Well
from schemas.graph_pressure import HydraulicResult
from utils.calculations.well_consraction import calculate_conductor_depth
from sqlalchemy import select
from models.graph_pressure import Info
from utils.calculations.colums import define_column


router = APIRouter()

@router.post("/well_conductor",
             response_model=ColumnResponse,
             tags=["well_constraction"])
def create_well_constraction(session: SessionDep, well_id: int,
                             params: ConductorInputParams)->ColumnResponse:
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    result = calculate_conductor_depth(params)
    db_obj = Construction(
        well_id=well_id,
        conductor_depth=result.conductor_depth
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return ColumnResponse.model_validate(db_obj)


@router.post("/well_columns",
             response_model=list[CasingDepth],
             tags=["well_constraction"])
def create_well_columns(session: SessionDep, well_id: int):
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = select(Info).where(Info.well_id==well_id).order_by(Info.depth_up_m)
    intervals_db = session.scalars(stmt).all()
    if not intervals_db:
        return []
    intervals = [HydraulicResult.model_validate(i) for i in intervals_db]
    results = define_column(intervals)
    construction = session.scalars(select(Construction).where(Construction.well_id == well_id)).first()
    db_objects = []
    for result in results:
        db_obj = CasingColumn(
            depth_m=result.depth,
            construction_id = construction.id
        )
        session.add(db_obj)
        db_objects.append(db_obj)
    session.commit()
    for obj in db_objects:
        session.refresh(obj)
    return results