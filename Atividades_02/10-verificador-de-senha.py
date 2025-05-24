'''
===========================================
10. VERIFICADOR DE SENHAS
===========================================

- Crie um programa que verifique se uma senha e forte. 
- Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um numero. 
- O programa deve continuar pedindo senhas ate que uma senha valida seja inserida ou o usuario digite 'sair'.
'''

while True:
    senha = input('Digite sua senha: ')

    if senha.lower() == 'sair':
        print('Programa encerrado. Até logo!')
        break

    print('Verificando senha...')

    if len(senha) < 8:
        print('Sua senha tem menos de 8 caracteres.\n')
        continue
    print('Sua senha tem 8 ou mais caracteres.')

    temNumero = False
    for caractere in senha:
        if caractere.isdigit():
            temNumero = True
            print('Número encontrado.')
            break

    if not temNumero:
        print('Sua senha não contém nenhum número.\n')
        continue
    print('Sua senha contém pelo menos um número.')

    print('Senha aprovada!!')
    break
