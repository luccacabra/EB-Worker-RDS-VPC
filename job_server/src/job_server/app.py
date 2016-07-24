import yaml

import tornado.ioloop
import tornado.gen
import tornado.web
from job_server.context import JobServerContext
from job_server.routes import PostJobHandler, RunJobHandler
from job_server.db import init_db


def job_server(context):
    return tornado.web.Application([
        (r'/job/run', RunJobHandler, dict(
            context=context
        )),
        (r'/job/post/([A-z]+)', PostJobHandler, dict(
            context=context
        ))
    ])


if __name__ == "__main__":
    context = JobServerContext(yaml.load(file('config.yaml', 'r')))
    init_db(context)
    app = job_server(context)
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
