from tornado.ioloop import IOLoop
from apscheduler.schedulers.tornado import TornadoScheduler
# Initialize the rest of the application here, or before the scheduler initialization.


class Job(object):
    
    def __init__(self, ioloop=None, tosp=None):
        self.ioloop = ioloop or IOLoop.current()
        self.scheduler = tosp or TornadoScheduler()
    
    def cron(self, *args, **kwargs):
        def wrapper(func):
            self.scheduler.add_job(func, 'interval', **kwargs)
            def _wrapper(*args, **kwargs):
                return func
            return _wrapper
        return wrapper
    
    def listen(self, *args, **kwargs):
        def wrapper(func):
            self.scheduler.add_listener(func, *args, **kwargs)
            def _wrapper(*args, **kwargs):
                return func
            return _wrapper
        return wrapper

    def run(self):
        self.scheduler.start()
        try:
            self.ioloop.start()
        except:
            pass
