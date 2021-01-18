class Job:
  def __init__(self, name, priority = 0):
    self.__pc = 0
    self.__acc = 0
    self.__program = []
    self.__mem = []
    self.__io = []
    self.__startting_time = -1
    self.__priority = 0
    self.__status = 'pending'
    with open(name, 'r') as new_job:
      line = new_job.readline()
      line = new_job.readline()
      self.__mem = [ 0 for _ in range(int(new_job.readline()[:-1])) ]
      line = new_job.readline()
      self.__io += new_job.readline()[:-1].split(',')
      line = new_job.readline()
      self.__io += new_job.readline()[:-1].split(',')
      line = new_job.readline()
      line = new_job.readline()
      while line:
        self.__program.append(line[:-1])
        line = new_job.readline()

  def getMem(self):
    return self.__mem

  def setMem(self, mem):
    self.__mem = [ x for x in mem]

  def getIo(self):
    return self.__io

  def getProgram(self):
    return self.__program

  def setProgram(self, program):
    self.__program = [ x for x in program ]

  def getPriority(self):
    return self.__priority

  def setBlock(self):
    self.__free = False

  def getStatus(self):
    return self.__status
  
  def setStatus(self, status):
    self.__status = status

  def setPc(self, value):
    self.__pc = value

  def setAcc(self, value):
    self.__acc = value

  def getPc(self):
    return self.__pc

  def getAcc(self):
    return self.__acc

  def incrementPc(self):
    self.__pc += 1

  