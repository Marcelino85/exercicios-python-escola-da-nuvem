'''
===========================================
8. CALCULADORA
===========================================
Desenvolva uma calculadora em Python que realize as quatro operacoes basicas entre dois numeros. 
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operacao. Siga as especificacoes abaixo:â€‹

- A calculadora deve solicitar ao usuario que insira dois numeros e uma operacao.â€‹
- As operacoes validas sao: + (adicao), - (subtracao), * (multiplicacao) e / (divisao).â€‹
- O programa deve continuar solicitando entradas ate que uma operacao valida seja concluida.â€‹

Trate os seguintes erros:â€‹

- Entrada invalida (nÃ£o numerica) para os numerosâ€‹
- Divisao por zeroâ€‹
- Operacao invalidaâ€‹
- Use try/except para capturar e tratar os erros apropriadamente.â€‹
- Apos cada erro, o programa deve informar o usuario sobre o erro e solicitar nova entrada.â€‹
- Quando uma operacao e concluida com sucesso, exiba o resultado e encerre o programa.â€‹
'''

print("CALCULADORA")
print("=" * 40)

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Operação inválida.")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2

        print(f"\nResultado: {num1:.0f} {operacao} {num2:.0f} = {resultado:.1f}")
        break  # Encerra o loop após operação bem-sucedida

    except ValueError as ve:
        print(f"Erro: {ve}. Por favor, tente novamente.\n")
    except ZeroDivisionError as ze:
        print(f"Erro: {ze}. Por favor, tente novamente.\n")
