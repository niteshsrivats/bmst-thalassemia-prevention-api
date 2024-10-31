from datetime import datetime
from typing import Optional

from pydantic import Field

from app.models.base_model import BaseDatabaseModel


class User(BaseDatabaseModel):
    id: str
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[str] = Field(None, alias="updatedAt")
    phone: Optional[str] = None

    def update(self, **kwargs):
        field_changed = False
        for key, value in kwargs.items():
            if getattr(self, key) != value:
                setattr(self, key, value)
                field_changed = True

        if field_changed:
            self.updated_at = datetime.utcnow().isoformat()

        return field_changed
