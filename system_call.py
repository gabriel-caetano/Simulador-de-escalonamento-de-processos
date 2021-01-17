from cpu import Cpu

class SystemCall:
	def __init__(self):
		self.__syscall = { "PARA": self.__stop, "LE": self.__read, "GRAVA": self.__write }

	def __stop(self, cpu, timer):
		cpu.setState("ilegal instruction")
		return False

	def __read(self, cpu, timer):
		cpu.saveState()
		cpu.sleep()
		with open("input.txt", 'r') as _input:
			value = _input.readline()
			cpu.setAcc(int(value))
		return True
	
	def __write(self, cpu, timer):
		cpu.saveState()
		cpu.sleep()
		with open("output.txt", 'w') as _output:
			_output.write(str(cpu.getAcc()))
		return True

	def execute(self, instruction, cpu, timer):
		try:
			self.__syscall[instruction](cpu, timer)
			return True
		except:
			return False
