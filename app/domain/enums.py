from enum import Enum

class ProjectStatus(str, Enum):
    open = 'open'
    in_progress = 'in_progress'
    completed = 'completed'
    cancelled = 'cancelled'
    
class UserRole(str, Enum):
    admin = 'admin'
    freelancer = 'freelancer'
    client = 'client'