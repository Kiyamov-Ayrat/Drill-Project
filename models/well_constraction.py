from sqlalchemy.orm import (relationship,
                            Mapped, mapped_column)
from sqlalchemy import ForeignKey

from models.data import Data


class Construction(Data):
    __tablename__ = "construction"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    well_id: Mapped[int] = mapped_column(ForeignKey("well.id"))

    column_depth: Mapped[float] = mapped_column(default=None)
    column_name: Mapped[str]

    well: Mapped["Well"] = relationship("Well", back_populates="construction")


    # columns: Mapped["CasingColumn"] = relationship("CasingColumn",
    #                                                back_populates="construction")

# class CasingColumn(Data):
#     __tablename__ = "casing_column"
#     id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     depth_m: Mapped[int]
#
#     construction_id: Mapped["Construction"] = mapped_column(ForeignKey("construction.id"))
#     construction: Mapped["Construction"] = relationship("Construction",
#                                                         back_populates="columns")