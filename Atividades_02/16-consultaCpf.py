'''
EXERCÍCIO PRÁTICO 16 
Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado.

Para esse exercicio consumir uma API viacep.com.br

'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado. Verifique se digitou corretamente.")
            return

        print("\n📍 Informações do Endereço:")
        print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
        print(f"Bairro:     {dados.get('bairro', 'Não disponível')}")
        print(f"Cidade:     {dados.get('localidade', 'Não disponível')}")
        print(f"Estado:     {dados.get('uf', 'Não disponível')}")

    except requests.exceptions.RequestException as e:
        print("Erro ao conectar à API:", e)

if __name__ == "__main__":
    print("🔎 Consulta de Endereço por CEP")
    cep = input("Digite o CEP (somente números): ").strip()

    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("CEP inválido. Deve conter 8 dígitos numéricos.")
