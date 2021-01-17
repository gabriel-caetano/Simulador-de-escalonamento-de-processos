class Controller:
	def run(self, cpu, so, timer):
		run = True
		while run:
			code = timer.getInterr()
			if code:
				so.resolveIlegal(cpu.getInstr())
				continue
			run = cpu.execute(cpu.getInstr())
			if not run:
				run = so.resolveIlegal(cpu.getInstr())
				if run:
					cpu.incrementPc()
					cpu.setCpuNormal()
			timer.increment()
