'''Faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais,
vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.'''

seg = int(input('Digita a quantidade de segundos que deseja converter: '))
a = seg // 86400  # 1 dia tem 86400 segundos
seg %= 86400
b = seg // 3600  # 1 hora tem 3600 segundos
seg %= 3600
c = seg // 60  # 1 minuto tem 60 segundos
seg %= 60
d = seg
print(f'{a} dias, {b} horas, {c} minutos e {d} segundos.')
