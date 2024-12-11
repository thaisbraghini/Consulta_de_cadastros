from flask import Flask, request
from flask_cors import CORS
import json
import os


app = Flask("Minha api")
CORS(app)
@app.route("/consulta")
def consulta_cadastro():
    print("Consulta de cadastro")
    documento = request.args.get('documento')
    registro = dados(documento)
    return registro

@app.route("/cadastro" , methods = ['POST'])
def cadastrarcliente():
    payload = request.json
    print(payload)
    cpf = payload.get("cpf")
    valores = payload.get("dados")
    salva_dados(cpf,valores)
    return "Dados cadastrados"

def carregar_arquivo():
    #caminho de onde o arquivo está salvo
    caminho_arquivo = os.path.realpath("EstruturadedadosAlysson/apiflask/dados.json")
    try:
        with open(caminho_arquivo) as arq:
            return json.load(arq)
    except Exception:
        return "Falha ao carregar o arquivo"

def gravar_arquivo(dados):
    caminho_arquivo = os.path.realpath("EstruturadedadosAlysson/apiflask/dados.json")
    try: 
        with open(caminho_arquivo, "w") as arq:
            json.dump(dados, arq, indent=4)
        return "dados armazenados"
    except Exception:
        return "falha ao gravar o arquivo"

def salva_dados(cpf,registro):
    dados_pessoas = carregar_arquivo()
    dados_pessoas[cpf] = registro
    gravar_arquivo(dados_pessoas)
    
def dados(cpf):
    print(cpf)
    dados_pessoas = carregar_arquivo()
    vazio = {
        "nome": "Não encontrado",
        "data_nascimento": "Não encontrado",
        "email": "Não Encontrado"
        }
    cliente = dados_pessoas.get(cpf, "registro nao encontrado")
    return cliente
    

#def selection_sort(data):
    keys = list(data.keys())
    n = len(keys)
    for i in range(n):
        # Assume que o menor elemento é o atual
        min_index = i
        for j in range(i + 1, n):
            if keys[j] < keys[min_index]:
                min_index = j
        # Troca os valores das chaves
        keys[i], keys[min_index] = keys[min_index], keys[i]

    # Cria um dicionário ordenado com base nas chaves
    sorted_data = {key: data[key] for key in keys}
    return sorted_data

#def gravar_arquivo(dados):
    caminho_arquivo = os.path.realpath("EstruturadedadosAlysson/apiflask/dados.json")
    try: 
        # Ordenar os dados antes de salvar
        sorted_data = selection_sort(dados)
        with open(caminho_arquivo, "w") as arq:
            json.dump(sorted_data, arq, indent=4)
        return "dados armazenados"
    except Exception:
        return "falha ao gravar o arquivo"

if __name__ == "__main__":
    app.run(debug=True)
    


