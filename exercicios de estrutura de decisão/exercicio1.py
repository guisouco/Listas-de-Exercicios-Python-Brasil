""" Faça um programa que peça dois numero e imprima o maior deles """

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1>n2:
    print(f'{n1} é maior que {n2}.')
elif n2>n1:
    print(f'{n2} é maior que {n1}.')
else:
    print('Os numeros são iguais.')
