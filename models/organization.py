from typing import Optional, List
from sqlalchemy import Column, Integer, String, select

from app import Base, async_session


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    descriptions = Column(String, nullable=False)
    edrpou_code = Column(String, nullable=False, unique=True)

    @classmethod
    async def get_all_organizations_via_edrpou_code(cls, code: str) -> Optional["Organization"]:
        async with async_session() as session:
            result = await session.execute(select(cls).filter_by(edrpou_code=code))
            return result.scalars().first()

    @classmethod
    async def get_all_organizations_via_name(cls, name: str) -> Optional[List["Organization"]]:
        async with async_session() as session:
            result = await session.execute(select(cls).filter(cls.name.ilike("%foobar%")).order_by(cls.id))
            return result.scalars().all()

    @classmethod
    async def get_organizations(cls) -> Optional[List["Organization"]]:
        async with async_session() as session:
            result = await session.execute(select(cls).order_by(cls.id))
            return result.scalars().all()
