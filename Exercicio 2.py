'''Exercício 2
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Entrada de Dados:

Digite a primeira nota: 4
Digite a segunda nota: 5
Digite a terceira nota: 6
Digite a quarta nota: 7

Saída de Dados:

A média aritmética é 5.5'''

notas = []
for c in range(4):
    nota = notas.append(float(input(f'Digite a {c+1}º nota: ')))
soma = sum(notas)
media = soma / len(notas)
print(f'Amédia aritimética é igual a {media}')
