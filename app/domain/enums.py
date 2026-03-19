from enum import Enum


class ProjectStatus(str, Enum):
    draft = 'draft'
    published = 'published'
    in_progress = 'in_progress'
    completed = 'completed'
    cancelled = 'cancelled'
    on_hold = 'on_hold'


class UserRole(str, Enum):
    admin = 'admin'
    freelancer = 'freelancer'
    client = 'client'


class InvoiceStatus(str, Enum):
    draft = 'draft'
    issued = 'issued'
    pending = 'pending'
    paid = 'paid'
    overdue = 'overdue'
    cancelled = 'cancelled'


class ContractStatus(str, Enum):
    draft = 'draft'
    sent = 'sent'
    signed = 'signed'
    active = 'active'
    completed = 'completed'
    terminated = 'terminated'


class ProposalStatus(str, Enum):
    draft = 'draft'
    submitted = 'submitted'
    accepted = 'accepted'
    rejected = 'rejected'
    withdrawn = 'withdrawn'


class MilestoneStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'
    approved = 'approved'
    rejected = 'rejected'


class TimeEntryStatus(str, Enum):
    draft = 'draft'
    submitted = 'submitted'
    approved = 'approved'
    rejected = 'rejected'


class PaymentMethod(str, Enum):
    bank_transfer = 'bank_transfer'
    paypal = 'paypal'
    stripe = 'stripe'
    crypto = 'crypto'


class NotificationType(str, Enum):
    project_invitation = 'project_invitation'
    proposal_received = 'proposal_received'
    contract_signed = 'contract_signed'
    invoice_issued = 'invoice_issued'
    payment_received = 'payment_received'
    milestone_completed = 'milestone_completed'
    review_received = 'review_received'
