from flask import Flask
from Block import *
from Transaction import *
from ecdsa import SigningKey, NIST384p

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bem vindo a nossa criptomoeda"

@app.route("/generateKey")
def generateKey():
    arq = open ('key.txt', 'w')
    sk = createSigningKey ()
    arq.writelines(str(sk))
    arq.close()
    return "Key gerada e salva com sucesso"

@app.route("/coinbase")
def coinbase():
    return COINBASE

@app.route("/validatingTransactionId", methods=['POST'])
def validating(id, transaction):
    id = request.form['id']
    transaction = request.form['transaction']
    if id is type(int) and transaction is type(Transaction):
        if validatingTransactionId(id, transaction):
            return "Transação valida"
        else:
            return "Transação invalida"
    else:
        return "Erro"



if __name__ == "__main__":
    app.run()