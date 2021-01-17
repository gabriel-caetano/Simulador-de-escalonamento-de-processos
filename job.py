class Job:
  def __init__(self, name, priority = 0):
    self.__mem_size = 0
    self.__input = ''
    self.__output = ''
    self.__program = []
    self.__startting_time = 0
    self.__priority = 0
    with open(name, 'r') as new_job:
      line = new_job.readline()
      line = new_job.readline()
      self.__mem_size = int(new_job.readline())
      line = new_job.readline()
      self.__input = new_job.readline()
      line = new_job.readline()
      self.__output = new_job.readline()
      line = new_job.readline()
      line = new_job.readline()
      while line:
        self.__program.append(line[:-1])
        line = new_job.readline()

  def getMemSize(self):
    return self.__mem_size

  def getInput(self):
    return self.__input

  def getOutput(self):
    return self.__Output

  def getProgram(self):
    return self.__program

  def getPriority(self):
    return self.__priority