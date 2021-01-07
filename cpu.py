class Cpu:
	def __init__(self, mem_size = 50):
		self.__program_path = ''
		self.__pc = 0
		self.__acc = 0
		self.__state = "normal"
		self.__instructions = {"CARGI": self.__cargi, "CARGM": self.__cargm, "CARGX": self.__cargx , "ARMM": self.__armm, "ARMX": self.__armx, "SOMA": self.__soma, "DESVZ": self.__desvz, "NEG": self.__neg, "PARA": self.__stop}
		self.__instruction_memory = []
		self.__data_memory = [ 0 for _ in range(mem_size)]

	def __memoryFail(self):
		self.__state = "memoria invalida"
		print(f"Memoria invalida durante a execucao {self.getCurrInstruction()} na linha {self.__pc}")

	def __ilegalInstruction(self):
		print("Instrucao invalida:", self.getCurrInstruction())
		self.__state = "Instrucao ilegal"

	def __stop(self):
		self.__state = "Instrucao ilegal"

	def __cargi(self, value):
		value = int(value[0])
		self.__acc = int(value)
		# print("Acumulador recebe", value)
		self.__pc += 1

	def __cargm(self, value):
		value = int(value[0])
		if len(self.__data_memory) > value:
			self.__acc = self.__data_memory[value]
			# print("Acumulador recebe", self.__data_memory[value], "da memoria", value)
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
			# print("Acumulador recebe", self.__data_memory[index], "da memoria", index)
			self.__pc += 1
		else:
			self.__memoryFail()

	def __armm(self, value):
		value = int(value[0])
		if len(self.__data_memory) > value:
			self.__data_memory[value] = self.__acc
			# print("salvou valor", self.__acc, "na memoria", value)
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
		# print("Salva valor", self.__acc, "na memoria", index)
		self.__pc += 1
		
	def __soma(self, value):
		value = int(value[0])
		if len(self.__data_memory) > value:
			# print("Soma", self.__acc, "+", self.__data_memory[value])
			self.__acc += self.__data_memory[value]
			self.__pc += 1
		else:
			self.__memoryFail()
		
	def __desvz(self, value):
		value = int(value[0])
		if self.__acc == 0:
			# print("Desvia para", value)
			self.__pc = value
		else:
			# print("Nao desvia")
			self.__pc += 1
		
	def __neg(self):
		self.__acc = -self.__acc
		self.__pc += 1

	def readFile(self, file_path):
		self.__program_path = file_path
		with open(file_path) as file:
			self.__instruction_memory = [x[:-1] if x[-1]<='\n' else x for x in file]

	def saveState(self):
		save_content = f"{self.__program_path}\n{self.__pc}\n{self.__acc}\n{self.__state}\n"
		for data in self.__data_memory:
			save_content += f"{data},"
		save_content = save_content[:-1]+'\n'
		with open("swap.txt", 'w') as swap:
			swap.write(save_content)

	def loadState(self):
		with open("swap.txt") as swap:
			self.readFile(swap.readline()[:-1])
			self.__pc = int(swap.readline()[:-1])
			self.__acc = int(swap.readline()[:-1])
			self.__state = swap.readline()[:-1]
			self.__data_memory = [int(x) for x in swap.readline()[:-1].split(",")]

	def resetState(self):
		self.__program_path = ''
		self.__pc = 0
		self.__acc = 0
		self.__state = "normal"
		self.__instruction_memory = []
		self.__data_memory = [ 0 for _ in range(mem_size)]

	def run(self, n = 0):
		run = True
		if n <= 0:
			while run:
				run = self.execute(self.getCurrInstruction())
		else:
			for i in range(n):
				if not run:
					break
				run = self.execute(self.getCurrInstruction())

	def execute(self, instruction):
		params = instruction.split()
		name = params.pop(0)
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

	def showCpuState(self):
		print(self.__state)
	
	def setCpuNormal(self):
		self.__state = "normal"
		
	def getCurrInstruction(self):
		return self.__instruction_memory[self.__pc]