from controller import Controller
from cpu import Cpu
from system_call import SystemCall
from timer import Timer
from job import Job

class OperatingSystem:
	def __init__(self, jobs):
		self.__cpu = Cpu()
		self.__syscall = SystemCall()
		self.__controller = Controller()
		self.__timer = Timer()
		self.__jobs = []
		for job in jobs:
			self.__jobs.append(job)
		self.__jobs = sorted(self.__jobs, key=lambda x: x.getPriority())

	def loadJob(self):
		self.__cpu.loadJob(self.__jobs.pop(0))


	def start(self):
		while len(self.__jobs):
			print("rodou programa")
			self.loadJob()
			self.__controller.run(self.__cpu, self, self.__timer)

	def getInstr(self):
		return self.__cpu.getInstr()

	def getMem(self, index = -1):
		return (self.__cpu.getDataMemory(index))

	def resolveIlegal(self, instruction):
		return self.__syscall.execute(instruction, self.__cpu, self.__timer)
