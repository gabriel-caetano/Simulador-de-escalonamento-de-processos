from cpu import Cpu

class SystemCall:
	def __init__(self):
		self.__syscall = { "PARA": self.__stop, "LE": self.__read, "GRAVA": self.__write }

	def __stop(self, cpu, timer, job):
		job.__setStatus('finished')
		cpu.setState("ilegal instruction")
		return False

	def __read(self, cpu, timer, job):
		with open("input.txt", 'r') as _input:
			value = _input.readline(),
			cpu.setAcc(int(value))
		return True
	
	def __write(self, cpu, timer, job):
		with open("output.txt", 'w') as _output:
			_output.write(str(cpu.getAcc()))
		return True

	def execute(self, instruction, cpu, timer):
		try:
			self.__syscall[instruction](cpu, timer)
			return True
		except:
			return False

	def read(self, index, job, job_index):
		job.setPc(job.getPc() + 1)
		input_address = f'{job_index}{job.getIo()[index].strip()}'
		with open(input_address) as reading:
			job.setAcc(int(reading.readline()[:-1]))

	def write(self, index, job, job_index):
		job.setPc(job.getPc() + 1)
		output_address = f'{job_index}{job.getIo()[index].strip()}'
		with open(output_address, 'w') as writing:
			writing.write(str(job.getAcc()))