from pydantic import BaseModel, ConfigDict


class RecordCreate(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'name': 'Sample Record',
                'description': 'Some description',
            }
        }
    )


class RecordChangeStatus(BaseModel):
    id: int
    status: bool

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'status': True
            }
        }
    )


class RecordDelete(BaseModel):
    id: int

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
            }
        }
    )


class RecordUpdate(BaseModel):
    id: int
    name: str
    description: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'name': 'Updated Record',
                'description': 'Updated description',
            }
        }
    )

class RecordRead(BaseModel):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'example': {
                'id': 1,
            }
        }
    )

class RecordResponse(BaseModel):
    id: int
    name: str
    description: str
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'example': {
                'id': 1,
                'name': 'Sample Record',
                'description': 'Some description',
                'status': False,
            }
        }
    )
