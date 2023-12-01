n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2
mod = n1 % n2
print('A soma é {}, a subtração é {} e a multiplicação é {}'.format(s, su, m))
print('A divisão é {:.3f}, e a divisão inteira é {}'.format(d, di))  # {:.3f} é para colocar 3 casas depois do ponto
print('A potência é {} e o resto da divisão é {}'.format(ex, mod))
