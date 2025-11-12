from decimal import Decimal
from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base_model import BaseModel

class Product(BaseModel):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    dosage_per_m2: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)

    cultures: Mapped[list["Culture"]] = relationship("Culture", back_populates="product")
