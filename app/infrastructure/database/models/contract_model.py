
from sqlalchemy import Boolean, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base_model import BaseModel


class ContractModel(BaseModel):
    __tablename__ = 'contracts'

    terms: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    signed: Mapped[bool] = mapped_column(Boolean, default=False)

    project_id: Mapped[str] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
        index=True,
    )

    project = relationship("ProjectModel", back_populates="contracts")

    invoices = relationship(
        "InvoiceModel",
        back_populates="contract",
        cascade="all, delete-orphan"
    )
