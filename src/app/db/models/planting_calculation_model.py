# app/db/models/planting_calculation_model.py
from decimal import Decimal
from sqlalchemy import Integer, Numeric, JSON, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base_model import BaseModel

class PlantingCalculation(BaseModel):
    __tablename__ = "planting_calculation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    culture_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("culture.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("product.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )

    total_area_m2: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    planting_area_m2: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    number_of_streets: Mapped[int] = mapped_column(Integer, nullable=False)
    product_qty: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)

    input_params: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[str] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False
    )

    # relações
    culture = relationship("Culture")
    product = relationship("Product")

    def __repr__(self) -> str:
        return f"<PlantingCalculation id={self.id} culture_id={self.culture_id} area={self.planting_area_m2}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "culture_id": self.culture_id,
            "product_id": self.product_id,
            "total_area_m2": str(self.total_area_m2),
            "planting_area_m2": str(self.planting_area_m2),
            "number_of_streets": self.number_of_streets,
            "product_qty": str(self.product_qty),
            "input_params": self.input_params,
            "created_at": self.created_at,
        }
