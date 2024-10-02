# Este é o arquivo de entrada principal para desenvolvimento. Comece lendo o README.md.
import mean_var_std  # Importa o módulo mean_var_std onde está a função calculate()
from unittest import main  # Importa a biblioteca unittest para rodar os testes unitários

# Teste básico da função calculate com uma lista de 9 números
# A função retorna um dicionário contendo as estatísticas da matriz 3x3
print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Executa automaticamente os testes unitários definidos no arquivo test_module.py
main(module='test_module', exit=False)