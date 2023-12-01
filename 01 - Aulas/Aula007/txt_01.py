nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}'.format(nome))  # :10 coloca o nome em 20 espaços
print('Prazer em te conhecer {:>20}'.format(nome))  # o sinal de > indica a direção que irá ficar
print('Prazer em te conhecer {:^20}'.format(nome))  # o sinal de ^ centraliza o conteúdo
print('Prazer em te conhecer {:=^20}'.format(nome))  # centraliza o conteúdo com a adição dos sinais de igual