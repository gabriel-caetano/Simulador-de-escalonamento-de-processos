class Controller:
	def run(self, cpu, so, timer):
		run = True
		while run:
			instr = cpu.getInstr()
			run = cpu.execute(instr)
			timer.increment()
			code = timer.getInterr()
			if code != -1:
				so.resolveInterruption(code)	
				continue
			if not run:
				so.resolveIlegal(cpu.getInstr(), cpu)
				run = True
			job = so.getScheduler().getJob(so.getScheduler().getIndex())
			if job.getStatus() == 'finished' or job.getStatus() == 'sleep':
				(next_job, finished) = so.getScheduler().getNext()
				if next_job:
					cpu.loadJob(next_job)
				elif finished:
					run = False
