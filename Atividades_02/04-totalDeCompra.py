''' 
===========================================
4. TOTAL DA COMPRA
===========================================

Objetivo:
Calcular o valor total a ser pago por um determinado numero de unidades de um produto.

Instrucoes:
- Escreva um programa que armazene o nome de um produto, seu preco unitario e a quantidade comprada.
- Calcule o valor total da compra e apresente uma descricao detalhada da transacao.

Explicacao:
- O valor total e obtido multiplicando o preco unitario pela quantidade comprada.
- Alem do calculo, a clareza na apresentacao das informacoes e essencial para a compreensao do usuario.
- O programa deve fornecer uma visao geral da compra, como se fosse um recibo simples.
'''

nomeProduto = 'Notebook'
precoUnitario = float(2000)
quantidade = 2
valorTotal = precoUnitario * 2

print(f'---Recibo de compra---\n')
print(f'Produto:{nomeProduto}')  
print(f'Preço Unitário: R$ {precoUnitario :.2f}')      
print(f'Quantidade: {quantidade}')      
print(f'Valor Total: R$ {valorTotal :.2f}')      