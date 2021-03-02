from job import Job

class Scheduler:
  def __init__(self, jobs):
    self.__jobs = jobs
    self.__curr_index = -1

  def getNext(self):
    jobs = [job for i,job in enumerate(self.__jobs) if i != self.__curr_index]
    value = -1
    curr = -1
    index = -1
    finished = False
    for i, job in enumerate(self.__jobs):
      if job.getPriority() > curr:
        if job.getStatus() == 'normal':
          curr = job.getPriority()
          value = job
          index = i
    if index != -1:
      value.setStatus('running')
      self.__curr_index = index
    else:
      finished = True
      for job in self.__jobs:
        status = job.getStatus()
        notFinished = status != 'finished'
        notIlegal = status != 'Ilegal instruction'
        notMemory = status != 'Invalid memory'
        if notFinished and notIlegal and notMemory:
          finished = False
          break
    
    return (value, finished)

  def getIndex(self):
    return self.__curr_index

  def getQuant(self):
    return len(self.__jobs)

  def setFree(self, index):
    self.__jobs[index].setStatus('normal')

  def getJob(self, index):
    try:
      return self.__jobs[index]
    except:
      return None
