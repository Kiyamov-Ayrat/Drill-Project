from fastapi import APIRouter, HTTPException

from models.well import Well
from schemas.well import WellResponse, WellCreate
from database.data import SessionDep

router = APIRouter()

@router.post('/well', response_model=WellResponse)
def create_well(session: SessionDep, well_data: WellCreate):
    db_well = Well(**well_data.model_dump())
    session.add(db_well)
    session.commit()
    session.refresh(db_well)
    return WellResponse.model_validate(db_well)
@router.get('/well', response_model=WellResponse)
def get_well(session: SessionDep, well_id: int):
    db_well = session.get(Well, well_id)
    if db_well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    return WellResponse.model_validate(db_well)