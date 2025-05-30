import os
import json
import csv

def escrever_txt(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print("✔ Texto escrito com sucesso!")

def ler_txt(caminho):
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            print("📄 Conteúdo do TXT:")
            print(arquivo.read())
    else:
        print("Arquivo não encontrado.")

def escrever_csv(caminho, dados):
    with open(caminho, "w", newline='', encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Nome", "Idade"])
        writer.writerows(dados)
    print("✔ Dados CSV escritos com sucesso!")

def ler_csv(caminho):
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                print("🔹", linha)
    else:
        print("Arquivo não encontrado.")

def escrever_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print("✔ JSON escrito com sucesso!")

def ler_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print("📄 Conteúdo do JSON:")
            print(json.dumps(dados, indent=4, ensure_ascii=False))
    else:
        print("Arquivo não encontrado.")

# --- Programa Principal ---
tipo = input("Escolha o tipo de arquivo (txt, csv, json): ").lower()
acao = input("Digite 'ler' para leitura ou 'escrever' para escrita: ").lower()

caminho = input("Informe o nome do arquivo (ex: dados.txt, arquivo.json): ")

if tipo == "txt":
    if acao == "escrever":
        conteudo = input("Digite o texto para salvar no arquivo: ")
        escrever_txt(caminho, conteudo)
    elif acao == "ler":
        ler_txt(caminho)
    else:
        print("Ação inválida.")

elif tipo == "csv":
    if acao == "escrever":
        dados = []
        while True:
            nome = input("Digite um nome (ou 'sair' para finalizar): ")
            if nome.lower() == "sair":
                break
            idade = input("Digite a idade: ")
            dados.append([nome, idade])
        escrever_csv(caminho, dados)
    elif acao == "ler":
        ler_csv(caminho)
    else:
        print("Ação inválida.")

elif tipo == "json":
    if acao == "escrever":
        dados = {}
        while True:
            chave = input("Digite a chave (ou 'sair' para finalizar): ")
            if chave.lower() == "sair":
                break
            valor = input("Digite o valor: ")
            dados[chave] = valor
        escrever_json(caminho, dados)
    elif acao == "ler":
        ler_json(caminho)
    else:
        print("Ação inválida.")
else:
    print("Tipo de dado inválido. Escolha entre txt, csv ou json.")
