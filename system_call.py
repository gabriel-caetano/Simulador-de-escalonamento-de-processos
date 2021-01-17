from cpu import Cpu

class SystemCall:
	def __init__(self):
		self.__syscall = { "PARA": self.__stop, "LE": self.__read, "GRAVA": self.__write }

	def __stop(self, cpu: Cpu):
		cpu.setState("stop")

	def __read(self, cpu: Cpu):
		with open("0.txt", 'r') as _input:
			value = _input.readline()
			cpu.setAcc(int(value))
	
	def __write(self, cpu: Cpu):
		with open("1.txt", 'w') as _output:
			_output.write(str(cpu.getAcc()))

	def execute(self, instruction, cpu: Cpu):
		self.__syscall[instruction](cpu)

sys = SystemCall()
cpuu = Cpu(5)
sys.execute("LE", cpuu)
print(cpuu.getAcc())
