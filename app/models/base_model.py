from pydantic import BaseModel


class BaseDatabaseModel(BaseModel):
    class Config:
        # arbitrary_types_allowed = True
        from_attributes = True
        populate_by_name = True
        use_enum_values = False
