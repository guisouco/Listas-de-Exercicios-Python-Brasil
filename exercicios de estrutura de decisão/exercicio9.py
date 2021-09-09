"""Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1>n2 and n1>n3 and n2>n3:
    print(f'A ordem decrescente é {n1},{n2},{n3}')
elif n2>n3 and n2>n1 and n1>n3:
    print(f'A ordem decrescente é {n2}, {n1}, {n3}')
elif n3>n2 and n3>n1 and n2>n1:
    print(f'A ordem decrescente é {n3}, {n2}, {n1}')
elif n3>n1 and n3>n2 and n1>n2:
    print(f'A ordem decrescente é {n3}, {n1}, {n2}')
elif n1 == n2 and n2>n3:
    print(f'A ordem decrescente é {n1}, {n2}, {n3}')
elif n2 == n3 and n3>n1:
    print(f'A ordem decrescente é {n2}, {n3}, {n1}')
elif n3 == n1 and n3>n2:
    print(f'A ordem decrescente é {n3}, {n1}, {n2}')
else:
    print('Numeros iguais')

