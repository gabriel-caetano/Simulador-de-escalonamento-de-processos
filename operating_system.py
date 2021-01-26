from controller import Controller
from cpu import Cpu
from system_call import SystemCall
from timer import Timer
from scheduler import Scheduler

class OperatingSystem:
	def __init__(self, jobs):
		self.__cpu = Cpu()
		self.__syscall = SystemCall()
		self.__controller = Controller()
		self.__timer = Timer()
		self.__scheduler = Scheduler(jobs)
		
	def getScheduler(self):
		return self.__scheduler

	def start(self):
		(next_job, finished) = self.__scheduler.getNext()
		if next_job:
			self.__cpu.setCpuNormal()
			self.__cpu.loadJob(next_job)
			self.__controller.run(self.__cpu, self, self.__timer)

	def getInstr(self):
		return self.__cpu.getInstr()

	def getMem(self, index = -1):
		return (self.__cpu.getDataMemory(index))

	def resolveIlegal(self, instruction, cpu):
		if instruction.split()[0] == 'LE' or instruction.split()[0] == 'GRAVA':
			self.__cpu.sleep()
			self.__cpu.saveState(self.__scheduler.getJob(self.__scheduler.getIndex()))
			self.__timer.newInterr(0, self.__scheduler.getIndex(), 5)
		else:
			self.__scheduler.getJob(self.__scheduler.getIndex()).setStatus('finished')


	def resolveInterruption(self, code):
		self.__scheduler.setFree(code)
		job = self.__scheduler.getJob(code) 
		pc = job.getPc()
		instr = job.getProgram()[pc]
		if instr.split()[0] == 'LE':
			param = int(instr.split()[1])
			self.__syscall.read(param, job, code)
		elif instr.split()[0] == 'GRAVA':
			param = int(instr.split()[1])
			print("instr: ", instr)
			print("code: ", code)
			self.__syscall.write(param, job, code)
		if self.__cpu.getState() == 'sleep':
			(next_job, finished) = self.__scheduler.getNext()
			if next_job:
				self.__cpu.setCpuNormal()
				self.__cpu.loadJob(next_job)