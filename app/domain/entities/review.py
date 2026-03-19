from datetime import datetime
from typing import Optional
from uuid import UUID

from .base_entity import BaseEntity


class Review(BaseEntity):
    def __init__(
        self,
        id: UUID,
        rating: float,
        communication_rating: float,
        quality_rating: float,
        deadline_rating: float,
        comment: str,
        project_id: UUID,
        reviewer_id: UUID,
        reviewee_id: UUID,
        contract_id: UUID,
        created_at: datetime,
        is_public: bool = True,
        responded_at: Optional[datetime] = None,
        response: Optional[str] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.project_id = project_id
        self.reviewer_id = reviewer_id
        self.reviewee_id = reviewee_id
        self.contract_id = contract_id
        self.rating = rating
        self.communication_rating = communication_rating
        self.quality_rating = quality_rating
        self.deadline_rating = deadline_rating
        self.comment = comment
        self.is_public = is_public
        self.responded_at = responded_at
        self.response = response
