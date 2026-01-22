from models.data import Data
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class ConstructionDiameter(Data):
    __tablename__ = "construction_diameter"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    well_id: Mapped[int] = mapped_column(ForeignKey("well.id"))

    column_depth: Mapped[float] = mapped_column()
    column_name: Mapped[str] = mapped_column()
    column_diameter: Mapped[float] = mapped_column()
    bit_diameter: Mapped[float] = mapped_column()

    well: Mapped["Well"] = relationship("Well", back_populates='construction_diameter')