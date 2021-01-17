class Controller:
	def run(self, cpu, so, timer):
		run = True
		while run:
			timer.increment()
			run = cpu.execute(cpu.getInstr())
			if not run:
				run = so.resolveIlegal(cpu.getInstr())
				if run:
					cpu.incrementPc()
					cpu.setCpuNormal()
