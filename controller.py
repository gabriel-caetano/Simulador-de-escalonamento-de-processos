class Controller:
	def run(self, cpu, so, timer):
		run = True
		while run:
			print("programa:", so.getScheduler().getIndex())
			instr = cpu.getInstr()
			print("instrucao:", instr)
			print("timer:", timer.getTime())
			run = cpu.execute(instr)
			timer.increment()
			if not run:
				so.resolveIlegal(cpu.getInstr(), cpu)
				run = True
			code = timer.getInterr()
			if code != -1:
				so.resolveInterruption(code)	
				continue
			job = so.getScheduler().getJob(so.getScheduler().getIndex())
			if job.getStatus() == 'finished' or job.getStatus() == 'sleep':
				(next_job, finished) = so.getScheduler().getNext()
				print("finished?", finished, next_job)
				if next_job != -1:
					cpu.loadJob(next_job)
				elif finished:
					run = False
