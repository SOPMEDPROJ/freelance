from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table 
from sqlalchemy.dialects.postgresql import ARRAY
from .user import *
metadata = MetaData()
product = Table(
    "product",
    metadata,
    Column("id",Integer, primary_key=True, unique=True),
    Column("title", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("timing", String, nullable=True),
    Column("ownerId", ForeignKey(user.c.id)),
    Column("owner", String, nullable=False),
    Column("img", String, nullable=True),
    Column("descr", String, nullable=False),
    Column("type", String, nullable=False),
    Column("status", String, nullable=True),
    Column("theme", String, nullable=True),
    
)

basa = Table(
    "base",
    metadata,
    Column("id", Integer, unique=True, primary_key=True),
    Column("bio", String, nullable=False),
    Column("date", String, nullable=False),
    Column("img", String, nullable=True),
    Column("descr", String, nullable=True),
    Column("client", Boolean, default=False),
    Column("implementer", Boolean, default=False),
    Column("listOfOrders", ARRAY(Integer),nullable=True),
    Column("listOfServices", ARRAY(Integer), nullable=True),
)