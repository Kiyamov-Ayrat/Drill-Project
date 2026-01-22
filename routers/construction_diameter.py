from fastapi import APIRouter, HTTPException
from database.data import SessionDep
from models.well import Well
from utils.calculations.casing_diameter import calculate_diameters
from schemas.construction_diameter import Diameter
from sqlalchemy import select, delete
from models.construction_diameter import ConstructionDiameter

router = APIRouter()

@router.post("/diameter/{well_id}",
            tags=["diameter"],
             response_model=list[Diameter])
def calculate_construction_diameters(session: SessionDep, well_id: int, first_diameter: int) -> list[Diameter]:
    return calculate_diameters(session=session, well_id=well_id, first_diameter=first_diameter)

@router.get("/diameter/{well_id}",
            tags=["diameter"],
            response_model=list[Diameter])
def get_construction_diameters(session: SessionDep, well_id: int) -> list[Diameter]:
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = select(ConstructionDiameter).where(ConstructionDiameter.well_id == well.id)
    diameters_db = session.scalars(stmt).all()
    if not diameters_db:
        raise HTTPException(status_code=404, detail="Diameters not found")
    return [Diameter.model_validate(diameters) for diameters in diameters_db]

@router.delete("/diameter/{well_id}",
               tags=["diameter"])
def delete_construction_diameters(session: SessionDep, well_id: int):
    well = session.get(Well, well_id)
    if well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    stmt = delete(ConstructionDiameter).where(ConstructionDiameter.well_id == well.id)
    result = session.execute(stmt)
    session.commit()
    return {"success": True}