class Controller:
	def run(self, cpu, so, timer):
		run = True
		count = 0
		while run:
			print(f'---------------------')
			print(f'iteracao: {count}')
			count += 1
			timer.increment()
			code = timer.getInterr()
			print(f'job state? {so.getScheduler().getJob(so.getScheduler().getIndex()).getStatus()}')
			print(f'cpu state? {cpu.getState()}')
			if code != -1:
				print('interrupcao?', code if code > -1 else 'nao')
				so.resolveInterruption(code)
				continue
			run = cpu.execute(cpu.getInstr())
			print(f'run? {run}')
			if not run:
				so.resolveIlegal(cpu.getInstr(), cpu)
				run = True
			if so.getScheduler().getJob(so.getScheduler().getIndex()).getStatus() == 'finished':
				next_job = so.getScheduler().getNext()
				if next_job:
					cpu.loadJob(next_job)
				else:
					run = False
