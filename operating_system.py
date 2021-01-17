from controller import Controller
from cpu import Cpu
from system_call import SystemCall
from timer import Timer

class OperatingSystem:
	def __init__(self):
		self.__cpu = Cpu(10)
		self.__syscall = SystemCall()
		self.__controller = Controller()
		self.__timer = Timer()

	def load(self, prog_name):
		self.__cpu.readFile(prog_name)

	def start(self):
		self.__controller.run(self.__cpu, self, self.__timer)

	def getInstr(self):
		return self.__cpu.getInstr()

	def getMem(self, index = -1):
		return(self.__cpu.getDataMemory(index))

	def resolveIlegal(self, instruction):
		return self.__syscall.execute(instruction, self.__cpu)