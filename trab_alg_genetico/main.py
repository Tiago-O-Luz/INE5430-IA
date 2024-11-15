#! alg_gen/bin/python

import numpy  # Biblioteca para operações matemáticas com arrays
import pygad  # Biblioteca para Algoritmos Genéticos em Python
from fitness import *  # Importa a função fitness e dados dos itens

# Define a função fitness utilizada pelo algoritmo genético
fitness_function = fitness_func

# Número de gerações para a evolução
num_generations = 50

# Número de pais selecionados para cruzamento em cada geração
num_parents_mating = 5

# Número de indivíduos (soluções) na população
sol_per_pop = 10

# Número de genes em cada solução, que corresponde ao número de itens
num_genes = len(items)

# Intervalo para inicialização dos genes (0 ou 1, pois é uma escolha binária para cada item)
init_range_low = 0
init_range_high = 1

# Método de seleção dos pais: "rws" (Roulette Wheel Selection)
parent_selection_type = "rws"

# Número de pais mantidos na próxima geração
keep_parents = 1

# Tipo de crossover utilizado: "uniform", onde cada gene é escolhido aleatoriamente de um dos pais
crossover_type = "uniform"

# Tipo de mutação utilizado: "random", onde genes são alterados aleatoriamente
mutation_type = "random"

# Percentual de genes a serem mutados em cada indivíduo
mutation_percent_genes = 10

# Espaço dos genes: [0, 1], indicando que o gene pode ser apenas 0 ou 1 (escolher ou não o item)
gene_space = [0, 1]

# Tipo dos genes: int (inteiro), representando a escolha binária de inclusão de itens
gene_type = int

# Criação da instância do algoritmo genético com os parâmetros definidos
ga_instance = pygad.GA(
    num_generations=num_generations,              # Número de gerações
    num_parents_mating=num_parents_mating,        # Número de pais para cruzamento
    fitness_func=fitness_function,                # Função fitness
    sol_per_pop=sol_per_pop,                      # Número de soluções por população
    num_genes=num_genes,                          # Número de genes por solução (número de itens)
    init_range_low=init_range_low,                # Intervalo de inicialização (baixo)
    init_range_high=init_range_high,              # Intervalo de inicialização (alto)
    parent_selection_type=parent_selection_type,  # Tipo de seleção de pais
    keep_parents=keep_parents,                    # Número de pais mantidos
    crossover_type=crossover_type,                # Tipo de crossover
    mutation_type=mutation_type,                  # Tipo de mutação
    mutation_percent_genes=mutation_percent_genes,# Percentual de genes a serem mutados
    gene_type=gene_type,                          # Tipo de genes
    gene_space=gene_space                         # Espaço dos genes
)

# Executa o algoritmo genético
ga_instance.run()

# Obtém a melhor solução encontrada pelo algoritmo genético
solution, solution_fitness, solution_idx = ga_instance.best_solution()

# Imprime os parâmetros da melhor solução
print("Parameters of the best solution : {solution}".format(solution=solution))

# Imprime o valor de fitness da melhor solução
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

# Calcula o valor total dos itens selecionados na melhor solução
value = sum([v * items[i][1] for i, v in enumerate(solution)])

# Imprime o valor total dos itens selecionados
print("Predicted output based on the best solution : {prediction}".format(prediction=value))