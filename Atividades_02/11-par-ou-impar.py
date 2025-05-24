'''
===========================================
11. PAR OU IMPAR
===========================================

Crie um programa que solicite ao usuario que insira numeros inteiros. 
O programa deve continuar solicitando numeros ate que o usuario digite 'fim'. 
Para cada numero inserido, o programa deve informar se e par ou impar. 
Se o usuario inserir algo que nao seja um numero inteiro, o programa deve informar o erro e continuar. 
No final, o programa deve exibir a quantidade de numeros pares e impares inseridos.
'''

quantidadePares = 0
quantidadeImpares = 0

while True:
    entrada = input('Digite um número inteiro ou "fim" para sair: ')

    if entrada.lower() == 'fim':
        print('\nPrograma encerrado.\n')
        break
    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f'O número {numero} é PAR\n')
            quantidadePares += 1
        else:
            print(f'O número {numero} é ÍMPAR\n')
            quantidadeImpares += 1
    except ValueError:
        print('Erro: entrada inválida. Digite um número inteiro ou "fim".\n')

print(f'Quantidade de números PARES: {quantidadePares}')
print(f'Quantidade de números ÍMPARES: {quantidadeImpares}')
