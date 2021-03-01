class Controller:
	def run(self, cpu, so, timer):
		run = True
		while run:
			timer.increment()
			instr = cpu.getInstr()
			run = cpu.execute(instr)
			if not run:
				so.resolveIlegal(instr, cpu)
				run = True
			code = timer.getInterr()
			interrupted = code != -1
			while code != -1:
				so.resolveInterruption(code)	
				code = timer.getInterr()
				continue
			if interrupted:
				continue
			job = so.getScheduler().getJob(so.getScheduler().getIndex())
			if job.getStatus() == 'finished' or job.getStatus() == 'sleep':
				(nextJob, finished) = so.getScheduler().getNext()
				i = 0
				while True:
					job = so.getScheduler().getJob(i)
					if not job:
						break
					i += 1
				if nextJob != -1:
					cpu.loadJob(nextJob)
					nextJob.setStarttingTime(timer.getTime())
				elif finished:
					run = False

