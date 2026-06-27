from dataclasses import dataclass


@dataclass
class RegistrationResult:
    document_id: str
    created: bool