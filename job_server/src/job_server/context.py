from boto3.session import Session
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

class JobServerContext:
    def __init__(self, config):
        self.aws_region_name = config['aws']['region_name']
        self.aws_session = Session(region_name=self.aws_region_name)
        self.sqs = self.aws_session.resource('sqs',
                                             endpoint_url=self.aws_session.client('sqs')
                                             .get_queue_url(QueueName=config['aws']['sqs']['queue_name'])['QueueUrl']) \
            .get_queue_by_name(QueueName=config['aws']['sqs']['queue_name'])
        self.engine = create_engine(str(URL(config['database']['engine'],
                                            username=config['database']['user'],
                                            password=config['database']['password'],
                                            host=config['database']['host'],
                                            port=config['database']['port'],
                                            database=config['database']['database_name'])))
        self.sql = self.engine.connect
        self.session_factory = sessionmaker(bind=self.engine)
