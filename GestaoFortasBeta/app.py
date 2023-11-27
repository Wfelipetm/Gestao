# Importações necessárias
from flask import Flask, render_template, redirect, url_for, flash
from config import DB_URI
from models.models import db
from views.crud_cadastro_veiculos import cadastrar_veiculo, deletar_veiculo, editar_veiculo, obtertodos_veiculos
from views import index
from sqlalchemy.exc import IntegrityError

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configuração da URI do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Chave para o alert!
app.secret_key = '3ec3f66c3e0a4a4b93a5c578b3b1972d'

# Inicializa a extensão SQLAlchemy com o aplicativo Flask
db.init_app(app)

# Adiciona esta linha para configurar a pasta templates
app.template_folder = 'templates'

# Com o contexto do aplicativo, cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/obtertodos_veiculos')
def obtertodos_veiculos_route():
    return obtertodos_veiculos()

@app.route('/cadastrar_veiculo', methods=['GET', 'POST'])
def cadastrar_veiculo_route():
    return cadastrar_veiculo()

@app.route('/editar_veiculo/<int:id>', methods=['GET', 'POST'])
def editar_veiculo_route(id):
    return editar_veiculo(id)

@app.route('/deletar_veiculo/<int:id>')
def deletar_veiculo_route(id):
    return deletar_veiculo(id)






# Configuração Global
if __name__ == '__main__':
    # Inicia o aplicativo Flask
    app.run(host='0.0.0.0', port='5000', debug=True)
