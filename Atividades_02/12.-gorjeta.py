'''
===========================================
12. GORJETA
===========================================

Enunciado: 
Crie uma funcao que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.â€‹

â€‹ParÃ¢metros:â€‹

- valor_conta (float): O valor total da contaâ€‹
- porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)â€‹

â€‹Retorna:â€‹
O valor da gorjeta calculadaâ€‹â€‹
'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
print(calcular_gorjeta(69.9, 10))  # Deve imprimir 6.99
