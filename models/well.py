from sqlalchemy.orm import (Mapped, mapped_column, relationship)
from models.data import Data

class Well(Data):
    __tablename__ = 'well'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    intervals: Mapped[list["Info"]] = (
        relationship("Info",back_populates="well",
                     cascade="all, delete-orphan"))
    construction: Mapped[list["Construction"]] = (
        relationship("Construction",
                     back_populates="well",
                     cascade="all, delete-orphan"))

    construction_diameter: Mapped[list["ConstructionDiameter"]] = (
        relationship("ConstructionDiameter",
                     back_populates="well",
                     cascade="all, delete-orphan")
    )