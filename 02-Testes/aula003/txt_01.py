n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
# print('A soma entre ', n1, 'e', n2, ' vale', s)                #  formato antigo do Python
print('A soma entre {} e {} vale {}'.format(n1, n2, s))    # sintaxe nova


# print(type(n1))     type - ver o tipo primitivo
