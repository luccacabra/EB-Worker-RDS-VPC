import datetime
import logging

from job_server.db import JobServerData

LOG = logging.getLogger(__name__)


class BaseJob:
    def __init__(self, session):
        self.session = session

    def run(self, **kwargs):
        pass


class CronJob(BaseJob):
    def __init__(self, session):
        super(CronJob, self).__init__(session)

    def run(self, **kwargs):
        LOG.info('Cron Job Triggered at ({timestamp})'.format(
            timestamp=str(datetime.datetime.now())
        ))


class InsertJob(BaseJob):
    def __init__(self, session):
        super(InsertJob, self).__init__(session)

    def run(self, **kwargs):
        data = kwargs.get('data')
        self.session.insert(JobServerData(data=data))
