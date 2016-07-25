from sqlalchemy import BIGINT, Column, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists

BASE = declarative_base()
TABLE_ID = Sequence('table_id_seq', start=1000)

class JobServerData(BASE):
    __tablename__ = 'job_server_data'

    id = Column(BIGINT, TABLE_ID, primary_key=True, nullable=False, server_default=TABLE_ID.next_value())
    data = Column(String())

def init_db(context):
    # Ensure db exists
    if not database_exists(context.engine.url):
        create_database(context.engine.url)

        # Create Tables
        BASE.metadata.create_all(context.engine)
