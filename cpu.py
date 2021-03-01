from job import Job

class Cpu:
	def __init__(self):
		self.__pc = 0
		self.__acc = 0
		self.__state = "sleep"
		self.__instructions = {"CARGI": self.__cargi, "CARGM": self.__cargm, "CARGX": self.__cargx , "ARMM": self.__armm, "ARMX": self.__armx, "SOMA": self.__soma, "DESVZ": self.__desvz, "NEG": self.__neg}
		self.__instruction_memory = []
		self.__data_memory = []

	def __memoryFail(self):
		self.__state = "invalid memory"
		print(f"Memoria invalida durante a execucao {self.getInstr()} na linha {self.__pc}")

	def __ilegalInstruction(self):
		self.__state = "finished"

	def __cargi(self, value):
		value = int(value[0])
		self.__acc = int(value)
		self.__pc += 1

	def __cargm(self, value):
		value = int(value[0])
		if len(self.__data_memory) > value:
			self.__acc = self.__data_memory[value]
			self.__pc += 1
		else:
			self.__memoryFail()

	def __cargx(self, value):
		value = int(value[0])
		value_in_range = len(self.__data_memory) > value
		range_in_range = len(self.__data_memory[self.__data_memory[value]]) > self.__data_memory[value]
		if value_in_range and range_in_range:
			index = self.__data_memory[value]
			self.__acc = self.__data_memory[index]
			self.__pc += 1
		else:
			self.__memoryFail()

	def __armm(self, value):
		value = int(value[0])
		if len(self.__data_memory) > value:
			self.__data_memory[value] = self.__acc
			self.__pc += 1
		else:
			self.__memoryFail()
		
	def __armx(self, value):
		value = int(value[0])
		value_in_range = len(self.__data_memory) > value
		range_in_range = len(self.__data_memory[self.__data_memory[value]]) > self.__data_memory[value]
		if value_in_range and range_in_range:
			index = self.__data_memory[value]
			self.__data_memory[index] = self.__acc
		self.__pc += 1
		
	def __soma(self, value):
		value = int(value[0])
		if len(self.__data_memory) > value:
			self.__acc += self.__data_memory[value]
			self.__pc += 1
		else:
			self.__memoryFail()
		
	def __desvz(self, value):
		value = int(value[0])
		if self.__acc == 0:
			self.__pc = value
		else:
			self.__pc += 1
		
	def __neg(self):
		self.__acc = -self.__acc
		self.__pc += 1

	def loadJob(self, job):
		self.__pc = job.getPc()
		self.__acc = job.getAcc()
		self.__data_memory =  [ x for x in job.getMem() ]
		self.__instruction_memory = [ x for x in job.getProgram() ]
		self.__state = 'normal'
		
	def saveState(self, job):
		job.setPc(self.__pc)
		job.setAcc(self.__acc)
		job.setMem(self.__data_memory)
		job.setStatus(self.__state)

	def loadState(self):
		with open("swap.txt") as swap:
			self.readFile(swap.readline().replace('\n',''))
			self.__pc = int(swap.readline().replace('\n',''))
			self.__acc = int(swap.readline().replace('\n',''))
			self.__state = swap.readline().replace('\n','')
			self.__data_memory = [int(x) for x in swap.readline().replace('\n','').split(",")]
			line = swap.readline().replace('\n','')
			instru = []
			while line:
				instru.append(line)
				line = swap.readline().replace('\n','')
			
	def resetState(self):
		self.__program_path = ''
		self.__pc = 0
		self.__acc = 0
		self.__state = "normal"
		self.__instruction_memory = []
		self.__data_memory = [ 0 for _ in range(mem_size) ]

	def execute(self, instruction):
		if not instruction:
			return False
		params = instruction.split()
		name = params.pop(0)
		if self.__state == 'sleep':
			return True

		if self.__state != "normal":
			return False
		if len(params) == 0:
			try:
				self.__instructions[name]()
				return True
			except:
				self.__ilegalInstruction()
				return False
		elif len(params) > 0:
			try:
				self.__instructions[name](params)
				return True
			except:
				self.__ilegalInstruction()
				return False

	def getDataMemory(self, index = -1):
		if index < 0:
			return self.__data_memory
		elif index < len(self.__data_memory):
			return self.__data_memory[index]
		else:
			self.__memoryFail()

	def showInstructionMemory(self, index = -1):
		if index < 0:
			print(self.__instruction_memory)
		elif index < len(self.__instruction_memory):
			print(self.__instruction_memory[index])
		else:
			self.__memoryFail()

	def getState(self):
		return self.__state
	
	def setCpuNormal(self):
		self.__state = "normal"
		
	def getInstr(self):
		try:
			return self.__instruction_memory[self.__pc]
		except:
			return None

	def getAcc(self):
		return self.__acc

	def setAcc(self, value):
		self.__acc = value

	def incrementPc(self):
		self.__pc += 1

	def getPc(self):
		return self.__pc

	def sleep(self):
		self.__state = 'sleep'

	def getProgram(self):
		return self.__instruction_memory
