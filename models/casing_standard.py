from sqlalchemy.orm import Mapped, mapped_column
from models.well import Data

class Casing(Data):
    __tablename__ = "casing"
    id: Mapped[int] = mapped_column(primary_key=True)
    diameter: Mapped[int]
    thickness: Mapped[float]
