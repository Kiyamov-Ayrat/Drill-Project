from sqlalchemy.orm import (DeclarativeBase,
                            Mapped, mapped_column, relationship)

class Data(DeclarativeBase):
    pass

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