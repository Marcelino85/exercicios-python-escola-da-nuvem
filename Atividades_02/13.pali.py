'''
===========================================
13. PALINDROMO
===========================================

Crie uma funcao que verifique se uma palavra ou frase e um palindromo 
(le-se igual de tras para frente, ignorando espacos e pontuacao). 
Se o resultado E True, responda â€œSimâ€, se o resultado for False, responda â€œNao"
'''
import string

def verificar_palindromo(texto):
    # Remove espaços, pontuação e coloca tudo em minúsculas
    texto_limpo = ''.join(
        caractere.lower() for caractere in texto if caractere.isalnum()
    )

    # Verifica se é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
    

print(verificar_palindromo("Ame a ema"))               # Sim
print(verificar_palindromo("Socorram-me, subi no ônibus em Marrocos"))  # Sim
print(verificar_palindromo("Python"))                  # Não

