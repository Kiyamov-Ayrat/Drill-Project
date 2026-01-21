from models.data import Data
from sqlalchemy.orm import Mapped, mapped_column


class Bit(Data):
    __tablename__ = "bit"
    id: Mapped[int] = mapped_column(primary_key=True)
    diameter: Mapped[float] = mapped_column()
    type: Mapped[str] = mapped_column()