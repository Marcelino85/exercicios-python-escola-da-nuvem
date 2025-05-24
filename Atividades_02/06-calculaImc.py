'''
===========================================
6. CALCULADORA DE IMC
===========================================

Enunciado:
Desenvolva um programa que calcule o Indice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros), calcular o IMC e informar a classificacao de acordo com a tabela padrao.

Instrucoes:
- Solicite os dados do usuario: peso e altura.
- Calcule o IMC usando a formula: IMC = peso / (altura ** 2).
- Exiba o valor do IMC com uma casa decimal e a respectiva classificacao (ex: abaixo do peso, normal, sobrepeso etc.).

Explicacao:
- O exercicio envolve entrada de dados numericos com ponto flutuante, calculos matematicos e estruturas condicionais.
- A classificacao deve seguir os intervalos padrao definidos para o IMC.
- Apresente o resultado de forma clara e arredondado corretamente.
'''
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.1f}.")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Eutrófico (Peso normal)")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade grau I")
elif imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III (grave)")
