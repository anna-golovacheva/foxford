import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class StatusType(Enum):
    open = 'open'
    in_progress = 'in_progress'
    closed = 'closed'

class Status(BaseModel):
    status: StatusType


class TicketRetrieve(BaseModel):
    id: int
    status: StatusType
    client_id: int
    employee_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    message: str


class TicketListResponse(BaseModel):
    status: str
    data: Optional[List[TicketRetrieve]]
    details: Optional[str]


class TicketRetrieveResponse(BaseModel):
    status: str
    data: Optional[TicketRetrieve]
    details: Optional[str]


class TicketUpdate(BaseModel):
    id: int
    status: StatusType


class TicketUpdateResponse(BaseModel):
    status: str
    data: Optional[TicketUpdate]
    details: Optional[str]