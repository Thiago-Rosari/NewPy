a = input('Digite algo: ')
tipo_primitivo = type(a)

print(f'O tipo primitivo desse valor é: {tipo_primitivo}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Todas em maiúsculas? {a.isupper()}')
print(f'Todas em minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')