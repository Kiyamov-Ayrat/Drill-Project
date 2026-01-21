from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.data import Data

class StandardCasingDiameter(Data):
    __tablename__ = "standard_casing_diameter"
    id: Mapped[int] = mapped_column(primary_key=True)
    diameter: Mapped[int] = mapped_column()
    coupling_diameter: Mapped[float |None] = mapped_column()

    thickness: Mapped[list["WallThickness"]] = (
        relationship("WallThickness",
                     back_populates="diameter"))

class WallThickness(Data):
    __tablename__ = "wall_thickness"
    id: Mapped[int] = mapped_column(primary_key=True)
    thickness: Mapped[float] = mapped_column()
    diameter_id: Mapped[int] = mapped_column(ForeignKey("standard_casing_diameter.id"))

    diameter: Mapped["StandardCasingDiameter"] = relationship("StandardCasingDiameter",
                                                              back_populates="thickness")
