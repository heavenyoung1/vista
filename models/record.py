from ._base import Base

from sqlalchemy import String, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column

class Record(Base):
    __tablename__ = 'records'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[bool] = mapped_column(Boolean)