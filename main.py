# Trabalho 1: simulador de escalonamento de processos
# Nome: Gabriel Vinicius Schmitt Caetano
from operating_system import OperatingSystem
from job import Job

job_1 = Job('job1')
job_2 = Job('job2')
job_3 = Job('job3')
jobs = [job_1, job_2, job_3]


so = OperatingSystem(jobs)
so.start()
instr = so.getInstr()
mem = so.getMem(0)
status = []

i = 0
while True:
  job = so.getScheduler().getJob(i)
  if not job:
    break
  print(f'status job {i}: {job.getStatus()}')
  print(f'job start: {job.getStarttingTime()}')
  i += 1

  status.append(job.getStatus())


print()
print(f"O programa parou na instrucao {instr}.")
print(f"O valor de m[0] e {mem}")
