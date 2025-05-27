'''
EXERCÍCIO PRÁTICO 15
Crie um programa que gera um perfil de usuário aleatório usando a API
'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado."
'''

import requests

res = requests.get('https://randomuser.me/api/')
dados = res.json()

usuario = dados['results'][0]
nome = f'{usuario['name']['first']} {usuario['name']['last']}'
email = usuario['email']
pais = usuario['location']['country']

print(f'{nome}')
print(f'{email}')
print(f'{pais}')