"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terceiro numero: '))

if n1>n2 and n3:
    maior = n1
    if n3>n2:
        menor = n2
    else:
        menor = n3

if n2>n3 and n1:
    maior = n2
    if n3>n1:
        menor = n1
    else:
        menor = n3

if n3>n2 and n1:
    maior = n3
    if n2>n1:
        menor = n1
    else:
        menor = n2

print(f'O valor maior é {maior} e o valor menor é {menor}')