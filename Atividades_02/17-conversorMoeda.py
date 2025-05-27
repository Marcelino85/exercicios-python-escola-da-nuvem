'''
EXERCÍCIO PRÁTICO 17

Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.

site API: https://docs.awesomeapi.com.br/api-de-moedas
'''

import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        par = f"{moeda}BRL"
        if par not in dados:
            print(f"Moeda '{moeda}' não encontrada. Verifique o código.")
            return
        
        cotacao = dados[par]
        
        nome = cotacao['name']
        valor_atual = float(cotacao['bid'])
        valor_max = float(cotacao['high'])
        valor_min = float(cotacao['low'])
        timestamp = int(cotacao['timestamp'])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")
        
        print(f"\nCotação de {nome}")
        print(f"Valor atual: R$ {valor_atual:.2f}")
        print(f"Valor máximo do dia: R$ {valor_max:.2f}")
        print(f"Valor mínimo do dia: R$ {valor_min:.2f}")
        print(f"Última atualização: {data_hora}")
    
    except requests.exceptions.RequestException as e:
        print("Erro ao conectar à API:", e)

if __name__ == "__main__":
    print("Consulta de Cotação de Moeda")
    codigo = input("Informe o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()
    consultar_cotacao(codigo)
