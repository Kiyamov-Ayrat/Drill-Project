# from sqlalchemy.orm import (DeclarativeBase,
#                             Mapped, mapped_column)
#
#
# class Base(DeclarativeBase):
#     pass

# class Pressure(Base):
#     __tablename__ = "pressure"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     density: Mapped[int]
#     depth: Mapped[int]
#     pressure: Mapped[int]




# class PressureCreate(BaseModel):
#     density: int
#     depth: int
#
# class PressureUpdate(BaseModel):
#     density: int | None = None
#     depth: int | None = None
#     # pressure: int | None = None
#
#     model_config = ConfigDict(from_attributes=True)
#
# class PressureResponse(PressureCreate):
#     id: int
#     pressure: int
#
#     class Config:
#         from_attributes = True