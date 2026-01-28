from fastapi import APIRouter, HTTPException, status

from models.well import Well
from schemas.well import WellResponse, WellCreate
from database.data import SessionDep
from sqlalchemy import delete

router = APIRouter()

@router.post('/well',
             response_model=WellResponse,
             tags=["well"])
async def create_well(session: SessionDep, well_data: WellCreate):
    db_well = Well(**well_data.model_dump())
    session.add(db_well)
    await session.commit()
    await session.refresh(db_well)
    return WellResponse.model_validate(db_well)
@router.get('/well',
            response_model=WellResponse,
            tags=["well"])
async def get_well(session: SessionDep, well_id: int):
    db_well = await session.get(Well, well_id)
    if db_well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    return WellResponse.model_validate(db_well)

@router.delete('/well',
               status_code=status.HTTP_204_NO_CONTENT,
               tags=["well"])
async def delete_well(session: SessionDep, well_id: int):
    db_well = await session.get(Well, well_id)
    if db_well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    await session.delete(db_well)
    await session.commit()
    return {"success": True}