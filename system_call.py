from cpu import Cpu

class SystemCall:
	def read(self, index, job, job_index):
		job.setPc(job.getPc() + 1)
		input_address = f'jobs/{job.getName()}/io/{job.getIo()[index].strip()}'
		count = job.getIoCount()[index]
		with open(input_address) as reading:
			line = reading.readlines()
			job.setAcc(int(line[count]))

		job.incrementCount(index)

	def write(self, index, job, job_index):
		job.setPc(job.getPc() + 1)
		output_address = f'jobs/{job.getName()}/io/{job.getIo()[index].strip()}'
		count = job.getIoCount()[index]
		line = str(job.getAcc()) + '\n'
		if count:
			with open(output_address, 'a') as writing:
				writing.write(line)
		else:
			with open(output_address, 'w') as writing:
				writing.write(line)
		job.incrementCount(index)
