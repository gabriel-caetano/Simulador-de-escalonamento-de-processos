
class Controller:
	def run(self, cpu, so):
		run = True
		while run:
			run = cpu.execute(cpu.getInstr())
			if not run:
				run = so.resolveIlegal(cpu.getInstr())
				if run:
					cpu.incrementPc()
					cpu.setCpuNormal()
