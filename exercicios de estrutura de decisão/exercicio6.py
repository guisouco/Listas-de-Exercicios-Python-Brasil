"""Faça um Programa que leia três números e mostre o maior deles."""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terceiro numero: '))

if __name__ == '__main__':
    if n1>n2 and n1>n3:
        print(f'O {n1} é maior que {n2} e {n3}')
    elif n2>n1 and n2>n3:
        print(f'O {n2} é maior que {n1} e {n3}')
    elif n3>n1 and n3>n2:
        print(f'O {n3} é maior que {n2} e {n1}')
    else:
        print('Os numeros são iguais')