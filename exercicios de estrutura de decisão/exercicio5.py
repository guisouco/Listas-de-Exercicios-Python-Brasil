"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota_1_aluno = float(input('Digite a nota numero 1: '))
nota_2_aluno = float(input('Digite a nota numero 2: '))

print(f'Sua média foi {(nota_1_aluno + nota_2_aluno) / 2}')
if nota_1_aluno == 10:
  print('Aprovado com Distinção')
elif nota_1_aluno >= 7:
  print('Aprovado')
else:
  print('Reprovado')

  print('Finalizou o programa')