from fastapi import APIRouter, Depends
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.tickets.models import Ticket
from src.tickets.schemas import TicketListResponse, TicketRetrieve, \
    TicketRetrieveResponse, TicketUpdate, TicketUpdateResponse
from src.auth.config import fastapi_users
from src.tickets.schemas import StatusType
from src.tickets.config import SORTING


router = APIRouter(
    prefix='/ticket',
    tags=['Ticket']
)

current_active_user = fastapi_users.current_user(active=True)


@router.get('/list',
            response_model=TicketListResponse,
            dependencies=[Depends(current_active_user)])
async def get_ticket_list(
    status: str = None,
    employee_id: int = None,
    sort: str = None,
    limit: int = 20,
    offset: int = 0,
    session: AsyncSession = Depends(get_async_session)
    ):

    try:
        query = select(Ticket)
        if status:
            query = query.where(Ticket.status == status)
        if employee_id:
            query = query.where(Ticket.employee_id == employee_id)
        if sort in SORTING:
            query = query.order_by(sort)
        query = query.limit(limit).offset(offset)
        result = await session.execute(query)
        ticket_result = result.all()
        tickets = []
        for i in range (len(ticket_result)):
            tickets.append(ticket_result[i][0])
        resp_list = [
                TicketRetrieve(
                id=ticket.id,
                status=ticket.status,
                client_id=ticket.client_id,
                employee_id=ticket.employee_id,
                created_at=ticket.created_at,
                updated_at=ticket.updated_at,
                message=ticket.message
                ) for ticket in tickets]
        return TicketListResponse(
            status='success',
            data=resp_list,
            details=None
            )

    except Exception as e:
        return TicketListResponse(
            status='error',
            data=None,
            details=str(e)
            )


@router.get('/{ticket_id}',
            response_model=TicketRetrieveResponse,
            dependencies=[Depends(current_active_user)])
async def get_ticket(
    ticket_id: int = None,
    session: AsyncSession = Depends(get_async_session)
    ):

    try:
        query = select(Ticket).where(Ticket.id == ticket_id)
        result = await session.execute(query)
        ticket_result = result.first()
        if ticket_result:
            ticket_item = ticket_result[0]
            ticket = TicketRetrieve(
                id=ticket_item.id,
                status=ticket_item.status,
                client_id=ticket_item.client_id,
                employee_id=ticket_item.employee_id,
                created_at=ticket_item.created_at,
                updated_at=ticket_item.updated_at,
                message=ticket_item.message
                )

            return TicketRetrieveResponse(
                status='success',
                data=ticket,
                details=None
                )
        else:
            return TicketRetrieveResponse(
                status='error',
                data=None,
                details='Тикета с указанным id не существует'
                )

    except Exception as e:
        return TicketRetrieveResponse(
            status='error',
            data=None,
            details=str(e)
            )


@router.patch('/{ticket_id}/status-update',
              dependencies=[Depends(current_active_user)])
async def update_ticket_status(
    ticket_id: int,
    status: StatusType,
    session: AsyncSession = Depends(get_async_session)
    ):

    try:
        print(">>> from router file >>   ", session)
        query = update(Ticket).filter(Ticket.id == ticket_id).\
                               values({'status': status.value}). \
                               returning(Ticket.id, Ticket.status)
        result = await session.execute(query)
        await session.commit()
        values = list(result.iterator)[0]
        res = dict(zip(['id', 'status'], values))
        return TicketUpdateResponse(
            status='success',
            data=res,
            details=None
            )
    except Exception as e:
        return TicketUpdateResponse(
            status='error',
            data=None,
            details=str(e)
            )
