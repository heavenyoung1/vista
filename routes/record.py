from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_connect import get_session
from models.record import Record
from schemas.record import (
    RecordCreate,
    RecordChangeStatus,
    RecordUpdate,
    RecordDelete,
    RecordResponse,
)

# ========== Router ==========
router = APIRouter(prefix='/api/v0', tags=['record'])

@router.post(
    '/',
    response_model=RecordResponse,
    status_code=status.HTTP_201_CREATED,
    summary='Создание записи',
)
async def create_record(
    record: RecordCreate,
    db: AsyncSession = Depends(get_session),
):
    db_record = Record(**record.model_dump())
    db.add(db_record)
    await db.commit()
    await db.refresh(db_record)
    return db_record

@router.get(
    '/{record_id}',
    response_model=RecordResponse,
    status_code=status.HTTP_200_OK,
    summary='Получение записи по ID',
)
async def read_record(
    record_id: int,
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(select(Record).where(Record.id == record_id))
    record = result.scalar_one_or_none()
    if not record:
        raise HTTPException(status_code=404, detail='Not found')
    return record

@router.get(
    '/',
    response_model=list[RecordResponse],
    status_code=status.HTTP_200_OK,
    summary='Получение всех записей',
)
async def read_records(
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(select(Record))
    records = result.scalars().all()
    if not records:
        raise HTTPException(status_code=404, detail='Not found')
    return records

@router.patch(
    '/',
    response_model=RecordResponse,
    status_code=status.HTTP_200_OK,
    summary='Обновление записи',
)
async def update_record(
    record: RecordUpdate,
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(select(Record).where(Record.id == record.id))
    query_record = result.scalar_one_or_none()
    if not query_record:
        raise HTTPException(status_code=404, detail='Not found')
    query_record.name = record.name
    query_record.description = record.description
    await db.commit()
    await db.refresh(query_record)
    return query_record

@router.patch(
    '/change_status',
    response_model=RecordResponse,
    status_code=status.HTTP_200_OK,
    summary='Изменение статуса записи',
)
async def change_status(
    record: RecordChangeStatus,
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(select(Record).where(Record.id == record.id))
    query_record = result.scalar_one_or_none()
    if not query_record:
        raise HTTPException(status_code=404, detail='Not found')
    query_record.status = record.status
    await db.commit()
    await db.refresh(query_record)
    return query_record

@router.delete(
    '/{record_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Удаление записи',
)
async def delete_record(
    record_id: int,
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(select(Record).where(Record.id == record_id))
    query_record = result.scalar_one_or_none()
    if not query_record:
        raise HTTPException(status_code=404, detail='Not found')
    await db.delete(query_record)
    await db.commit()
