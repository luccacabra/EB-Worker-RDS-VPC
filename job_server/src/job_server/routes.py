import json

import tornado.gen
import tornado.web

from jobs import CronJob, InsertJob


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.context = kwargs.get('context', {})
        self.mapping = {
            'CronJob': CronJob,
            'InsertJob': InsertJob
        }


class PostJobHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, job_type, **kwargs):
        data = json.loads(self.request.body) if self.request.body else {}
        data['job_type'] = job_type
        self.context.sqs.send_message(
            MessageBody="%s" % data
        )


class RunJobHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        body = json.loads(self.request.body)
        job_cls = body.pop('job_type')
        job = self.mapping[job_cls]

        try:
            job_session = self.context.session_factory()
            job(job_session).run(**body)
        except Exception:
            job_session.rollback()
        finally:
            job_session.close()
            self.finish()
