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
		self.__timer.newInterr(1, -2, 1, 5)
		
	def getScheduler(self):
		return self.__scheduler

	def start(self):
		self.__controller.run(self.__cpu, self, self.__timer)

	def getInstr(self):
		return self.__cpu.getInstr()

	def getMem(self, index = -1):
		return (self.__cpu.getDataMemory(index))

	def resolveIlegal(self, instruction, cpu):
		if not instruction:
			return
		instr = instruction.split()[0]
		if instr == 'LE' or instr == 'GRAVA':
			self.__cpu.sleep()
			self.__cpu.saveState(self.__scheduler.getJob(self.__scheduler.getIndex()), self.__timer)
			self.__timer.newInterr(0, self.__scheduler.getIndex(), 5)
		else:
			job = self.__scheduler.getJob(self.__scheduler.getIndex())
			if instr == 'PARA':
				print(f'status: {job.getStatus()}')
				print(f'time: {self.__timer.getTime()}')
				job.setStatus('finished')
				job.setEnd(self.__timer.getTime())
			else:	
				print(cpu.getState())
				job.setStatus(cpu.getState())
				job.setEnd(self.__timer.getTime())


	def resolveInterruption(self, code):
		if code < -1:
			index = self.__scheduler.getIndex()
			if index >= 0:
				job = self.__scheduler.getJob(index)
				self.__cpu.saveState(job, self.__timer)
			(nextJob, finished) = self.__scheduler.getNext()
			if nextJob != -1:
				self.__cpu.loadJob(nextJob)
				nextJob.setStart(self.__timer.getTime())
		else:
			self.__scheduler.setFree(code)
			job = self.__scheduler.getJob(code) 
			pc = job.getPc()
			instr = job.getProgram()[pc]
			if instr.split()[0] == 'LE':
				param = int(instr.split()[1])
				self.__syscall.read(param, job, code)
			elif instr.split()[0] == 'GRAVA':
				param = int(instr.split()[1])
				self.__syscall.write(param, job, code)
			if self.__cpu.getState() == 'sleep':
				(next_job, finished) = self.__scheduler.getNext()
				if next_job != -1:
					self.__cpu.setCpuNormal()
					self.__cpu.loadJob(next_job)
