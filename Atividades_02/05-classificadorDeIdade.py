'''
===========================================
5. CLASSIFICADOR DE IDADE
===========================================

Enunciado:
Crie um programa que solicite a idade do usuario e classifique-o em uma das seguintes categorias:
- Crianca (0 a 12 anos)
- Adolescente (13 a 17 anos)
- Adulto (18 a 59 anos)
- Idoso (60 anos ou mais)

Instrucoes:
- Solicite que o usuario digite sua idade.
- O programa deve interpretar o valor digitado e classifica-lo de acordo com as faixas etÃ¡rias.
- O resultado da classificacao deve ser exibido de forma clara.

Explicacao:
- Esse exercicio utiliza estruturas condicionais para tomar decisoes baseadas em faixas numericas.
- Importante tratar casos invalidos, como idades negativas.
- A logica deve garantir que nenhuma faixa se sobreponha ou fique sem cobertura.
'''

# Receber idade do usuario
# converter a idade para numero
# verificar a faixa etária de idade para o número informado
# lidar com numero negativo
# exibir o resultado na tela

idade = int(input('Informe a sua idade: '))

if idade >= 60:
    print('Você é uma pessoa idosa')
elif idade >= 18:
    print('Você é uma  pessoa adulta.')
elif idade >= 13:
    print('Você é uma  adolescente.')
elif idade >= 0:
    print('Você é uma  criança.')
else:
    print('Idade inválida.')
