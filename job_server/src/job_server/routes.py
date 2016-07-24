import json
import sys

import tornado.gen
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.context = kwargs.get('context', {})


class PostJobHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, job_type, **kwargs):
        yield self.context.sqs.send_message({
            'job_type': job_type
        })


class RunJobHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        body = json.loads(self.request.body)
        job_cls = body.pop('job_type')
        job = getattr(sys.modules[__name__], job_cls)

        try:
            job_session = self.context.session_factory()
            job(job_session).run(**body)
        except Exception:
            job_session.rollback()
        finally:
            job_session.close()
            self.finish()
