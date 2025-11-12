from decimal import Decimal
from sqlalchemy import String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base_model import BaseModel

class Culture(BaseModel):
    __tablename__ = "culture"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)

    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("product.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    format_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("format_type.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    street_size_m: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)

    product: Mapped["Product"] = relationship("Product", back_populates="cultures")
    format_type: Mapped["FormatType"] = relationship("FormatType", back_populates="cultures")


    def __iter__(self):
        for key, value in vars(self).items():
            yield key, value

    def __repr__(self):
        return f"<Culture> id={self.id} name={self.name}"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "product_id": self.product_id, "format_id": self.format_id}