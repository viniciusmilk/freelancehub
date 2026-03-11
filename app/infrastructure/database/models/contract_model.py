#Contract Model
from sqlalchemy import (
    Boolean,
    Float,
    ForeignKey,
    String,
    CheckConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.infrastructure.database.base_model import BaseModel


class ContractModel(BaseModel):
    __tablename__ = 'contracts'
    __table_args__ = (
        CheckConstraint('value >= 0', name='check_value_non_negative'),
    )

    terms: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    signed: Mapped[bool] = mapped_column(Boolean, default=False)

    project_id: Mapped[str] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    
    freelancer_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    project = relationship("ProjectModel", back_populates="contracts")
    freelancer = relationship("UserModel", back_populates="contracts")

    invoices = relationship(
        "InvoiceModel",
        back_populates="contract",
        cascade="all, delete-orphan"
    )
