'''Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento,
o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos,
no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que,
como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.'''


nome = input('Dijite seu nome: ')
dia = input('Qual o dia de vencimento: ')
mes = input('Qual o mês de vencimento: ')
valor = input('Qual o valor da fatura: ')
print(f'Olá, {nome}')
print(f'A sua fatura com vencimento em {dia} de {mes} no valor de R${valor} está fechada.')
