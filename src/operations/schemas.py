import datetime
from typing import List, Optional
from pydantic import BaseModel



class OperationCreate(BaseModel):
    quantity: str
    figi: str
    instrument_type: str
    date: datetime.datetime
    type: str

    class Config:
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
        }


class OperationList(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime.datetime
    type: str


class OperationListResponse(BaseModel):
    status: str
    data: Optional[List[OperationList]]
    details: Optional[str]
