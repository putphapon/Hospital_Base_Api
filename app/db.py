import databases, sqlalchemy
from .config import settings

## Postgres Database
database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "base_user",
    metadata,
    sqlalchemy.Column("id" , sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("username" , sqlalchemy.String),
    sqlalchemy.Column("password" , sqlalchemy.String),
    sqlalchemy.Column("type", sqlalchemy.CHAR),
    sqlalchemy.Column("first_name" , sqlalchemy.String),
    sqlalchemy.Column("last_name" , sqlalchemy.String),
    sqlalchemy.Column("date_of_birth", sqlalchemy.String),
    sqlalchemy.Column("address", sqlalchemy.String),
    sqlalchemy.Column("sub_district", sqlalchemy.String),
    sqlalchemy.Column("district", sqlalchemy.String),
    sqlalchemy.Column("province", sqlalchemy.String),
    sqlalchemy.Column("postcode", sqlalchemy.String),
    sqlalchemy.Column("height" , sqlalchemy.String),
    sqlalchemy.Column("weight" , sqlalchemy.String),
    sqlalchemy.Column("pressure", sqlalchemy.String)
)

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)