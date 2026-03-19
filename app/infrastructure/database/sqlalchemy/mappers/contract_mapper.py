from uuid import UUID

from .....domain.entities import Contract
from ..models.contract_model import ContractModel
from .base_mapper import BaseMapper


class ContractMapper(BaseMapper[Contract, ContractModel]):
    @staticmethod
    def to_entity(model: ContractModel) -> Contract:
        return Contract(
            id=UUID(model.id),
            freelancer_id=UUID(model.freelancer_id),
            project_id=UUID(model.project_id),
            proposal_id=UUID(model.proposal_id),    
            terms=model.terms,
            value=model.value,
            status=model.status,
            signed=model.signed,
            signed_at=model.signed_at,
            started_at=model.started_at,
            completed_at=model.completed_at,
            termination_reason=model.termination_reason,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(entity: Contract) -> ContractModel:
        return ContractModel(
            id=str(entity.id),
            freelancer_id=str(entity.freelancer_id),
            project_id=str(entity.project_id),
            proposal_id=str(entity.proposal_id),
            status=entity.status,
            terms=entity.terms,
            value=entity.value,
            signed=entity.signed,
            signed_at=entity.signed_at,
            started_at=entity.started_at,
            completed_at=entity.completed_at,
            termination_reason=entity.termination_reason,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
