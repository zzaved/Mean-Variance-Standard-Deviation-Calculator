import numpy as np  # Importa a biblioteca Numpy, usada para manipulação eficiente de arrays e operações matemáticas

# Definição da função calculate, que recebe uma lista de números como argumento
def calculate(list_of_numbers):
    
    # Verifica se a lista tem exatamente 9 elementos. Se não tiver, levanta um erro
    if len(list_of_numbers) != 9:
        raise ValueError("A lista deve conter nove números.")  # Mensagem de erro informando o problema
    
    # Converte a lista de números em um array Numpy e reorganiza em uma matriz de 3x3
    matrix = np.array(list_of_numbers).reshape(3, 3)
    
    # Cria um dicionário para armazenar os resultados dos cálculos estatísticos
    calculations = {
        # Calcula a média para cada coluna (axis=0), cada linha (axis=1) e para toda a matriz
        'mean': [matrix.mean(axis=0).tolist(),  # Média por coluna
                 matrix.mean(axis=1).tolist(),  # Média por linha
                 matrix.mean().tolist()],       # Média de toda a matriz
        
        # Calcula a variância para colunas, linhas e matriz
        'variance': [matrix.var(axis=0).tolist(),  # Variância por coluna
                     matrix.var(axis=1).tolist(),  # Variância por linha
                     matrix.var().tolist()],       # Variância da matriz inteira
        
        # Calcula o desvio padrão para colunas, linhas e matriz
        'standard deviation': [matrix.std(axis=0).tolist(),  # Desvio padrão por coluna
                               matrix.std(axis=1).tolist(),  # Desvio padrão por linha
                               matrix.std().tolist()],       # Desvio padrão total
        
        # Calcula o valor máximo para colunas, linhas e matriz
        'max': [matrix.max(axis=0).tolist(),  # Máximo por coluna
                matrix.max(axis=1).tolist(),  # Máximo por linha
                matrix.max().tolist()],       # Máximo de toda a matriz
        
        # Calcula o valor mínimo para colunas, linhas e matriz
        'min': [matrix.min(axis=0).tolist(),  # Mínimo por coluna
                matrix.min(axis=1).tolist(),  # Mínimo por linha
                matrix.min().tolist()],       # Mínimo total
        
        # Calcula a soma dos elementos para colunas, linhas e matriz
        'sum': [matrix.sum(axis=0).tolist(),  # Soma por coluna
                matrix.sum(axis=1).tolist(),  # Soma por linha
                matrix.sum().tolist()]        # Soma de toda a matriz
    }

    # Retorna o dicionário contendo todas as estatísticas calculadas
    return calculations