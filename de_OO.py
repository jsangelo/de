import numpy as np

class DifferentialEvolution:
    def __init__(self, population_size, num_variables, max_generations):
        self.population_size = population_size
        self.num_variables = num_variables
        self.max_generations = max_generations
        self.population = self.initialize_population()
        self.pop_solution = np.zeros(population_size)
        self.evaluation_count = 0

    def initialize_population(self):
        """Inicializa a população com indivíduos aleatórios."""
        return [np.random.rand(self.num_variables) for _ in range(self.population_size)]

    def objective(self, weights):
        """Calcula o valor da função objetivo e incrementa o contador de avaliações."""
        self.evaluation_count += 1  # Incrementa o contador
        return np.sum(weights)  # Função objetivo

    def normalize_weights(self, weights):
        """Normaliza os pesos para que a soma seja igual a 1."""
        return weights / np.sum(weights)

    def optimize(self):
        """Executa o algoritmo de Evolução Diferencial."""
        for generation in range(self.max_generations):
            for i in range(self.population_size):
                self.population[i] = self.normalize_weights(self.population[i])
                self.pop_solution[i] = self.objective(self.population[i])  # Avaliação da função

    def get_evaluation_count(self):
        """Retorna o número total de avaliações da função objetivo."""
        return self.evaluation_count

# Parâmetros do problema
population_size = 10
num_variables = 8
max_generations = 100

# Cria uma instância do algoritmo DE
de_algorithm = DifferentialEvolution(population_size, num_variables, max_generations)

# Executa a otimização
de_algorithm.optimize()

# Imprime o número total de avaliações da função objetivo
print(f"Número total de avaliações da função objetivo: {de_algorithm.get_evaluation_count()}")
