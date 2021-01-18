# Trabalho 1: simulador de escalonamento de processos
# Nome: Gabriel Vinicius Schmitt Caetano
from operating_system import OperatingSystem
from job import Job

job_1 = Job('job1.txt')
job_2 = Job('job2.txt')
job_3 = Job('job3.txt')
jobs = [job_1, job_2]


so = OperatingSystem(jobs)
so.start()
instr = so.getInstr()
mem = so.getMem(0)
prog0 = so.getScheduler().getJob(0).getStatus()
prog1 = so.getScheduler().getJob(1).getStatus()
# prog2 = so.getScheduler().getJob(2).getStatus()

print(prog0, prog1)
print(f"O programa parou na instrucao {instr}.")
print(f"O valor de m[0] e {mem}")

