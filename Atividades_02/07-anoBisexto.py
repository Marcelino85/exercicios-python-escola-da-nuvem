'''
===========================================
7. VERIFICADOR DE ANO BISSEXTO
===========================================

Enunciado:
Faca um programa que determine se um ano inserido pelo usuario e bissexto ou nao.
Lembre-se:
- Um ano e bissexto se for divisivel por 4;
- Mas anos divisiveis por 100 so sao bissextos se tambem forem divisiveis por 400.

Instrucoes:
- Solicite que o usuario digite um ano.
- Verifique se ele e bissexto ou nao, de acordo com as regras descritas.
- Exiba uma mensagem informando se o ano e bissexto.

Explicacao:
- Este exercicio explora o uso de operadores logicos e condicionais compostos.
- Trata-se de uma aplicacao classica que ajuda a desenvolver o raciocinio para multiplas condicoes encadeadas.
- Teste com diferentes anos para validar a logica.
'''

ano = int(input('Informe o ano a ser verificado: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
