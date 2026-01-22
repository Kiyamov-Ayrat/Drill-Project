from fastapi import APIRouter
from database.data import SessionDep
from utils.calculations.casing_diameter import calculate_diameters
from schemas.construction_diameter import Diameter

router = APIRouter()

@router.post("/diameter",
            tags=["diameter"])
def get_construction_diameters(session: SessionDep, well_id: int, first_diameter: int) -> list[Diameter]:
    return calculate_diameters(session=session, well_id=well_id, first_diameter=first_diameter)