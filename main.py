# Importando a biblioteca Flask
from flask import Flask

# Criando uma instância do Flask
app = Flask(__name__)

# Definindo uma rota para a URL /oi
@app.route('/oi', methods=['GET'])
def oi():
    # Retornando a string "oi"
    return "oi"

# Executando o servidor se o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)