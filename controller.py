class Controller:
	def run(self, cpu, so, timer):
		run = True
		count = 0
		while run:
			print(f'---------------------')
			print(f'iteracao: {count}')
			print(f'job atual = {so.getScheduler().getIndex()}')
			count += 1
			timer.increment()
			code = timer.getInterr()
			instr = cpu.getInstr()
			print(f'instrucao no controller:{instr}')
			print(f'pc: {cpu.getPc()}')
			if code != -1:
				print('interrupcao?', code)
				so.resolveInterruption(code)	
				continue
			run = cpu.execute(instr)
			if not run:
				so.resolveIlegal(cpu.getInstr(), cpu)
				run = True
			job = so.getScheduler().getJob(so.getScheduler().getIndex())
			if job.getStatus() == 'finished' or job.getStatus() == 'sleep':
				(next_job, finished) = so.getScheduler().getNext()
				if next_job:
					cpu.loadJob(next_job)
				else:
					if finished:
						run = False
