from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_PATH = "api/database.json"

# Função para garantir que os dados sejam persistidos
def ler_dados():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(DB_PATH, "w") as f:
        json.dump(dados, f, indent=4)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = ler_dados()
    novo_usuario = request.json
    
    # Verifica se CPF já existe
    if any(u['cpf'] == novo_usuario['cpf'] for u in dados['usuarios']):
        return jsonify({"erro": "CPF já cadastrado"}), 400
        
    dados['usuarios'].append(novo_usuario)
    salvar_dados(dados)
    return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201

@app.route('/deposito', methods=['POST'])
def depositar():
    info = request.json
    dados = ler_dados()
    
    # Simulação simples: busca conta pelo CPF do usuário
    for conta in dados['contas']:
        if conta['usuario']['cpf'] == info['cpf']:
            conta['saldo'] += info['valor']
            salvar_dados(dados)
            return jsonify({"mensagem": "Depósito realizado", "novo_saldo": conta['saldo']}), 200
            
    return jsonify({"erro": "Conta não encontrada"}), 404

@app.route('/extrato/<cpf>', methods=['GET'])
def ver_extrato(cpf):
    dados = ler_dados()
    conta = next((c for c in dados['contas'] if c['usuario']['cpf'] == cpf), None)
    
    if conta:
        return jsonify({"titular": conta['usuario']['nome'], "saldo": conta['saldo']}), 200
    return jsonify({"erro": "Conta não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
