from .util.log import Log
from multiprocessing import Queue


_log = Log('worker')

# Function executed by workers in Workerpool expexts Workload instance
def worker_func(job):
    job.execute()
    return job.results
