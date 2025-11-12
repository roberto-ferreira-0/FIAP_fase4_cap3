from decimal import Decimal
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.base_model import BaseModel

class SystemParam(BaseModel):
    __tablename__ = "system_param"

    key: Mapped[str] = mapped_column("key", String(80), primary_key=True)
    value_str: Mapped[str | None] = mapped_column(String(4000))
    value_num: Mapped[Decimal | None] = mapped_column(Numeric(18, 4))

    def __repr__(self) -> str:
        return f"<SystemParam key={self.key}>"

    def to_dict(self) -> dict:
        return {"key": self.key, "value_str": self.value_str, "value_num": (str(self.value_num) if self.value_num is not None else None)}
