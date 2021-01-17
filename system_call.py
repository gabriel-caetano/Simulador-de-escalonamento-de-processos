from cpu import Cpu

class SystemCall:
	def __init__(self):
		self.__syscall = { "PARA": self.__stop, "LE": self.__read, "GRAVA": self.__write }

	def __stop(self, cpu):
		cpu.setState("ILEGAL INSTRUCTION")
		return False

	def __read(self, cpu):
		with open("0.txt", 'r') as _input:
			value = _input.readline()
			cpu.setAcc(int(value))
		return True
	
	def __write(self, cpu):
		with open("1.txt", 'w') as _output:
			_output.write(str(cpu.getAcc()))
		return True

	def execute(self, instruction, cpu):
		try:
			self.__syscall[instruction](cpu)
			return True
		except:
			return False
