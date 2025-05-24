'''
===========================================
14. IDADE EM ANOS
===========================================

Crie uma funcao que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

â€‹
'''

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Desconsiderando anos bissextos
    return idade_dias

print(calcular_idade_em_dias(1978))  # Aproximadamente 8760 dias
