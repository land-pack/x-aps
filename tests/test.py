import time
from xaps import Job
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

job = Job()
counter = 0


@job.cron(seconds=2, id='my_ak')
def myfunc():
    global counter
    print("Current time is >>{} --- counter={}".format(time.time(), counter))
    if counter > 4:
        assert 1==-1
    counter += 1


@job.listen(EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
def slack_notification(event):
    if event.exception:
        print("The job crashed :(")
    else:
        print("The job worked :)")




if __name__ == '__main__':
    job.run()
