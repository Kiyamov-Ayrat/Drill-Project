from fastapi import APIRouter, HTTPException
from database.data import SessionDep
from models.debit_standard import DebitStandard
from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

from pydantic import BaseModel, ConfigDict


class FirstDiameter(BaseModel):
    diameter: list[int]

    model_config = ConfigDict(from_attributes=True)

router = APIRouter()

@router.get("/first_diameter",
            tags=["diameter"])

def get_first_diameter(session: SessionDep, debit: int, fluid_type: str):
    stmt = (
        select(DebitStandard).
        options(selectinload(DebitStandard.diameters))
        .where(
            and_(
                DebitStandard.debit >= debit,
                DebitStandard.fluid_type == fluid_type
            )
        )
        .order_by(DebitStandard.debit.asc())
        .limit(1)
    )
    standard = session.scalars(stmt).first()
    if not standard:
        raise HTTPException(status_code=404, detail="No suitable diameters")

    diameters = [d for d in standard.diameters]
    if not diameters:
        raise HTTPException(status_code=404, detail="No suitable diameters")
    return diameters