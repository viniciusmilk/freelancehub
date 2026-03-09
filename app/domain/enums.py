from enum import Enum


class ProjectStatus(str, Enum):
    draft = 'draft'
    in_progress = 'in_progress'
    completed = 'completed'
    cancelled = 'cancelled'


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
