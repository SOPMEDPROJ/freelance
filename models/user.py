from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Boolean, Float, MetaData, Table, Column, String, Integer, JSON, ForeignKey, TIMESTAMP

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("bio", String, nullable=False),
    Column("phone", String, nullable=True),
    Column("client", Boolean, default=False),
    Column("role_id", ForeignKey(role.c.id)),
    Column("date", String, default=None),
    Column("descr", String, nullable=True),
    Column("implementer", Boolean, default=False),
    Column("listOfOrders", ARRAY(Integer), nullable=True),
    Column("rate", Float, default=0.0),
    Column("comments", String, nullable=True),
    Column("avatar", String, nullable=False),
    Column("pendingTasks", ARRAY(Integer), nullable=True),
    Column("activeBalance", Integer, default=0),
    Column("frozenBalance", Integer, default=0),
    Column("transactions", String, nullable=True),
    Column("activeTasks", ARRAY(Integer), nullable=True),
    Column("userStatus", String, nullable=False, default="Offline"),

    Column("email",String(length=320), unique=True, index=True, nullable=False),
    Column("hashed_password",String(length=1024), nullable=False),
    Column("is_active",Boolean, default=True, nullable=False),
    Column("is_superuser",Boolean, default=False, nullable=False),
    Column("is_verified",Boolean, default=False, nullable=False)
)