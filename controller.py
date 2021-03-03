class Controller:
	def run(self, cpu, so, timer):
		run = True
		while run:
			timer.increment()
			instr = cpu.getInstr()
			index = so.getScheduler().getIndex()
			print('------------------------------')
			print(f'timer: {timer.getTime()}')
			print(f'job: {so.getScheduler().getIndex()}')
			print(f'instruction: {instr}')
			if index == 0 and instr == 'PARA':
				print('AAAAAAAAAAAAAAAAAAAAAAAAAA O QUE HOUVE?')
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
			status = job.getStatus()
			if status == 'finished' or status == 'Ilegal instruction' or status == 'Invalid memory' or status == 'sleep':
				(nextJob, finished) = so.getScheduler().getNext()
				if nextJob != -1:
					cpu.loadJob(nextJob)
					nextJob.setStart(timer.getTime())
				elif finished:
					run = False

