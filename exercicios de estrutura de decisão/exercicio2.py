"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo"""

v = float(input('Digite um valor: '))

if __name__ == '__main__':
    if v>0:
        print('O valor é positivo.')
    elif v<0:
        print('O valor é negativo.')