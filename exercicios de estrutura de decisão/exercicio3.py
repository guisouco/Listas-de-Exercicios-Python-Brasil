"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".

Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = str(input('Digite a letra F ou M para descobrir seu sexo: ')).upper()

if letra == 'M':
    print('M - Sexo Masculino')
elif letra == 'F':
    print('F - Sexo Feminino')
else:
    print('Sexo invalido')