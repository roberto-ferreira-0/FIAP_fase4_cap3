from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base_model import BaseModel

class FormatType(BaseModel):
    __tablename__ = "format_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(120))

    cultures: Mapped[list["Culture"]] = relationship("Culture", back_populates="format_type")
