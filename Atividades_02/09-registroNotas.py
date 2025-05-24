'''
===========================================
9. REGISTRO DE NOTAS
===========================================
 Crie um programa que permita a um professor registrar as notas de uma turma. 
- O programa deve continuar solicitando notas ate que o professor digite 'fim'. 
- Notas vÃ¡lidas sÃ£o de 0 a 10. 
- O programa deve ignorar notas invalidas e continuar solicitando. 
- No final, deve exibir a mÃ©dia da turma. Notas = [] -> len(Notas)â€‹
'''

print("REGISTRO DE NOTAS")
print("=" * 40)

notas = []

while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()
    
    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.\n")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim' para encerrar.\n")

# Exibe a média
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\nQuantidade de notas registradas: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")
