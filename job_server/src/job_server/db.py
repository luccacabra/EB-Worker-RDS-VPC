from sqlalchemy import Column, BIGINT, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists

BASE = declarative_base()


class JobServerData(BASE):
    __tablename__ = 'job_server_data'

    id = Column(BIGINT, primary_key=True, nullable=False)
    data = Column(String())

def init_db(context):
    # Ensure db exists
    if not database_exists(context.engine.url):
        create_database(context.engine.url)

        # Open connection
        connection = context.sql()

        # Create Tables
        BASE.metadata.create_all(connection)
