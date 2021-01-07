# Simulador de escalonamento de processos

Implementação em python 3 de um simulador de escalonamento de processos

## Requisitos

`from cpu import Cpu`

## Utilização

- `cpu = Cpu(tamanho_da_memoria)`

retorna uma nova instância com alocacao estatica
da memoria conforme passado por parametro

- `cpu.readFile(caminho_do_arquivo)`

carrega um arquivo contendo instrucoes de um programa

- `cpu.saveState()`

salva o estado da cpu em um arquivo 'swap.txt'

- `cpu.loadState()`

carrega o estado da cpu de um arquivo 'swap.txt'

- `cpu.resetState()`

reseta todos os valores da cpu para o estado inicial

- `cpu.run(n=0)`

executa n instrucoes do programa carregado na cpu, se n <= 0
executa o programa até encontrar algum erro ou encerrar

- `cpu.execute(instrucao)`

executa a instrucao passada por parametro

- `cpu.showDataMemory(i=-1)`

printa no terminal o valor da memória de dados na posicao i
se i < 0 printa toda a memoria

- `cpu.showInstructionMemory(i=-1)`

printa no terminal o valor da memória de dados instrucoes na posicao i
se i < 0 printa toda a memoria

- `cpu.showCpuState()`

printa no terminal o estado atual do da cpu

- `cpu.setCpuNormal()`

define o estado da cpu como 'normal'

- `cpu.getCurrInstruction()`

retorna a instrucao atualmente apontada pelo pc
