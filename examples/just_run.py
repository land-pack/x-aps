import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
scheduler = BackgroundScheduler()

from datetime import datetime
import os
from tornado.ioloop import IOLoop
from apscheduler.schedulers.tornado import TornadoScheduler
# Initialize the rest of the application here, or before the scheduler initialization.

counter = 0 

def myfunc():
    global counter
    print("Current time is >>{} --- counter={}".format(time.time(), counter))
    if counter > 4:
        assert 1==-1
    counter += 1

#scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
scheduler.add_job(myfunc, 'interval', seconds=5, id='my_job_id')

def my_listener(event):
    if event.exception:
        print("The job crashed :(")
    else:
        print("The job worked :)")

#scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

#scheduler.start()


if __name__ == '__main__':
    scheduler = TornadoScheduler()
    scheduler.add_job(myfunc, 'interval', seconds=3)
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass
