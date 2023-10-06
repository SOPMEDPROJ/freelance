from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from dto import dto as DTO
from models.models import product, basa


routerS = APIRouter(
    prefix="/services",
    tags=["Services"]
)



@routerS.get('/get')
async def services_get(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.id == id)
    print(query)
    result = await session.execute(query)
    return result.mappings().all()

@routerS.post('/post')
async def service_post(product_dto: DTO.Product, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**product_dto.dict())
    await session.execute(stmt)
    await session.commit()
    return stmt


routerB = APIRouter(
    prefix='/base',
    tags=["Base"]
)

@routerB.post('/post')
async def base_post(base_dto: DTO.Basa, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(basa).values(**base_dto.dict())
    await session.execute(stmt)
    await session.commit()
    return stmt

@routerB.get('/get')
async def base_get(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(basa).where(basa.c.id == id)
    print(query)
    result = await session.execute(query)
    return result.mappings().all()