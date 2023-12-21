from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate, OperationListResponse, OperationList
from src.auth.config import fastapi_users

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)

current_active_user = fastapi_users.current_user(active=True)

@router.get('/', response_model=OperationListResponse)
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(query)
        a = result.all()
        operations = []
        for i in range (len(a)):
            operations.append(a[i][0])
        resp_list = [
                OperationList(
                id=oper.id,
                quantity=oper.quantity,
                figi=oper.figi,
                instrument_type=oper.instrument_type,
                date=oper.date,
                type=oper.type
                ) for oper in operations]
        return OperationListResponse(
            status='success',
            data=resp_list,
            details=None
            )

    except Exception as e:
        return OperationListResponse(
            status='error',
            data=None,
            details=str(e)
            )


@router.post('/', dependencies=[Depends(current_active_user)])
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        statement = insert(Operation).values(new_operation.model_dump())
        await session.execute(statement)
        await session.commit()
        return {
            'status': 'success',
            'data': None,
            'details': None
            }
    except Exception as e:
        return {
            'status': 'error',
            'data': None,
            'details': str(e)
            }