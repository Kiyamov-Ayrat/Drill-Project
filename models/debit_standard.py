from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.data import Data
from sqlalchemy import ForeignKey, Table, Column, Integer

debit_standard_association = Table(
    "debit_standard_association",
    Data.metadata,
    Column("debit_standard_id", Integer, ForeignKey("debit_standard.id"), primary_key=True),
    Column("diameter_id", Integer, ForeignKey("standard_casing_diameter.id"), primary_key=True),
)


class DebitStandard(Data):
    __tablename__ = 'debit_standard'

    id: Mapped[int] = mapped_column(primary_key=True)
    fluid_type: Mapped[str] = mapped_column()
    debit: Mapped[int] = mapped_column()

    diameters: Mapped[list["StandardCasingDiameter"]] = (
        relationship("StandardCasingDiameter",
                     secondary=debit_standard_association,
                     backref="debit_standard"))