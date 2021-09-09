"""Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

p1 = float(input('Preço do primeiro produto: '))
p2 = float(input('Preço do segundo produto: '))
p3 = float(input('Preço do terceiro produto: '))

if p1<p2:
    if p1<p3:
        print(f'Você deve comprar o primeiro produto com seu valor de R${p1}')
    else:
        print(f'Você deve comprar o terceiro produto com seu valor de R${p3}')
else:
    if p2<p3:
        print(f'Você deve comprar o segundo produto com seu valor de R${p2}')
    else:
        print(f'Você deve comprar o terceiro produto com seu valor de R${p3}')