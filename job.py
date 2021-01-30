class Job:
  def __init__(self, name, priority = 0):
    self.__name = name
    self.__pc = 0
    self.__acc = 0
    self.__program = []
    self.__mem = []
    self.__io = []
    self.__io_count = []
    self.__startting_time = -1
    self.__priority = 0.5
    self.__status = 'pending'
    with open(f'jobs/{name}/{name}.txt', 'r') as new_job:
      line = new_job.readline()
      line = new_job.readline()
      self.__mem = [ 0 for _ in range(int(new_job.readline().replace('\n',''))) ]
      line = new_job.readline()
      self.__io += new_job.readline().replace('\n','').split(',')
      line = new_job.readline()
      self.__io += new_job.readline().replace('\n','').split(',')
      self.__io_count = [ 0 for _ in self.__io ]
      line = new_job.readline()
      line = new_job.readline()
      while line:
        self.__program.append(line.replace('\n',''))
        line = new_job.readline()

  def getIoCount(self):
    return self.__io_count

  def incrementCount(self, index):
    self.__io_count[index] = self.__io_count[index] + 1


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

  def getName(self):
    return self.__name
