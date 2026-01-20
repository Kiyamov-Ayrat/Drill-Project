from sqlalchemy.orm import (Mapped, mapped_column,
                            relationship)
from sqlalchemy import ForeignKey

from models.data import Data

class Info(Data):
    __tablename__ = 'info'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    well_id: Mapped[int] = mapped_column(ForeignKey('well.id'))

    pressure_mpa: Mapped[float]
    depth_up_m: Mapped[int]
    depth_down_m: Mapped[int]
    anomaly_coefficient: Mapped[float]
    fracturing_pressure_mpa: Mapped[float]
    fracturing_coefficient: Mapped[float]
    fracturing_coefficient2: Mapped[float]
    mud_density: Mapped[float]

    well: Mapped["Well"] = relationship("Well", back_populates="intervals")