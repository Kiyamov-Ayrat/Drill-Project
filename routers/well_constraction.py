from fastapi import APIRouter, HTTPException

from models.well_constraction import Construction
from schemas.well_constraction import ColumnResponse, ConductorInputParams, CasingDepth
from database.data import SessionDep
from models.well import Well
from schemas.graph_pressure import HydraulicResult, HydraulicInput
from utils.calculations.well_consraction import calculate_conductor_depth
from sqlalchemy import select, delete
from models.graph_pressure import Info
from utils.calculations.colums import define_column


router = APIRouter()

@router.post("/well_conductor",
             response_model=ColumnResponse,
             tags=["well_construction"])
def create_conductor(session: SessionDep, well_id: int,
                             params: ConductorInputParams)->ColumnResponse:
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    result = calculate_conductor_depth(params)
    db_obj = Construction(
        well_id=well_id,
        column_depth=result.column_depth,
        column_name=result.column_name
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return ColumnResponse.model_validate(db_obj)

@router.get("/well_columns/{well_id}",
            response_model=list[ColumnResponse],
            tags=["well_construction"])
def get_columns(session: SessionDep, well_id: int) -> list[ColumnResponse]:
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = select(Construction).where(Construction.well_id == well_id)
    columns_db = session.scalars(stmt).all()
    if not columns_db:
        raise HTTPException(status_code=404, detail="Columns not found")
    return [ColumnResponse.model_validate(colum) for colum in columns_db]


@router.post("/well_columns",
             response_model=list[CasingDepth],
             tags=["well_construction"])
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
    db_objects = []
    for result in results:
        db_obj = Construction(
            well_id=well_id,
            column_depth=result.column_depth,
            column_name=result.column_name
        )
        session.add(db_obj)
        db_objects.append(db_obj)
    session.commit()
    for obj in db_objects:
        session.refresh(obj)
    return results

@router.post("/well_construction",
             response_model=list[CasingDepth],
             tags=["well_construction"])
def create_well_construction(session: SessionDep, well_id: int,
                             inputs: list[CasingDepth]):
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    db_objects = []
    for input_data in inputs:
        db_obj = Construction(
            well_id=well_id,
            column_depth=input_data.column_depth,
            column_name=input_data.column_name
        )
        session.add(db_obj)
        db_objects.append(db_obj)
    session.commit()
    return [CasingDepth.model_validate(db_obj) for db_obj in db_objects]


@router.delete("/well_columns/{well_id}/{column_name}",
               tags=["well_construction"])
def delete_column(session: SessionDep, well_id: int, column_name: str):
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = (delete(Construction).where(Construction.well_id==well_id).
            where(Construction.column_name==column_name))
    result = session.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="column not found")
    session.commit()
    return {"success": True,
            "deleted": column_name}