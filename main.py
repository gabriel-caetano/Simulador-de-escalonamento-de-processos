# Trabalho 1: simulador de escalonamento de processos
# Nome: Gabriel Vinicius Schmitt Caetano
# Implementacao de uma classe Cpu com os metodos acessiveis conforme se segue:
# - cpu = Cpu(tamanho_da_memoria) 
#		retorna uma nova instância com alocacao estatica
# 	da memoria conforme passado por parametro

# cpu.readFile(caminho_do_arquivo)
#		carrega um arquivo contendo instrucoes de um programa

#	cpu.saveState()
#		salva o estado do cpu em um arquivo 'swap.txt'

# cpu.loadState()
#		carrega o estado do cpu de um arquivo 'swap.txt'

# cpu.resetState()
#		reseta todos os valores do cpu para o estado inicial

# cpu.run(n=0)
#		executa n instrucoes do programa carregado na cpu, se n <= 0
# 	executa o programa até encontrar algum erro ou encerrar

# cpu.execute(instrucao)
#		executa a instrucao passada por parametro

# cpu.showDataMemory(i=-1)
#		printa no terminal o valor da memória de dados na posicao i
#		se i < 0 printa toda a memoria

# cpu.showInstructionMemory(i=-1)
#		printa no terminal o valor da memória de dados instrucoes na posicao i
#		se i < 0 printa toda a memoria

# cpu.showCpuState()
#		printa no terminal o estado atual do do cpu

# cpu.setCpuNormal()
#		define o estado do cpu como 'normal'

# cpu.getCurrInstruction()
#		retorna a instrucao atualmente apontada pelo pc

from operating_system import OperatingSystem

so = OperatingSystem()
so.load("program.txt")
so.start()


# program = Cpu(3)
# program.readFile("program.txt")
# program.run()
# print(program.getState())
# # program.showInstructionMemory()
# program.saveState()
# program.loadState()
# mem = program.getDataMemory(0)
# instr = program.getCurrInstruction()
instr = so.getInstr()
mem = so.getMem(0)

print(f"O programa parou na instrucao {instr}.")
print(f"O valor de m[0] e {mem}")

