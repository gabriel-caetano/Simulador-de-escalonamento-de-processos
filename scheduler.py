from job import Job

class Scheduler:
  def __init__(self, jobs):
    self.__jobs = jobs
    self.__curr_index = -1

  def getNext(self):
    value = 0
    curr = -1
    index = -1
    for i, job in enumerate(self.__jobs):
      if job.getPriority() > curr:
        if job.getStatus() == 'pending':
          curr = job.getPriority()
          value = job
          index = i
    if value:
      value.setStatus('running')
      self.__curr_index = index
    else:
      for i, job in enumerate(self.__jobs):
        if job.getPriority() > curr:
          if job.getStatus() == 'sleep':
            curr = job.getPriority()
            value = job
            index = i
      if value:
        self.__curr_index = index
    return value

  def getIndex(self):
    return self.__curr_index

  def getQuant(self):
    return len(self.__jobs)

  def setFree(self, index):
    self.__jobs[index].setStatus('pending')

  def getJob(self, index):
    return self.__jobs[index]
