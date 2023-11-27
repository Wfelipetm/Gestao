
from flask import redirect, render_template, request, url_for, flash
from sqlalchemy.exc import IntegrityError
from models.models import CadastroVeiculo, db
# Importações necessárias
from sqlite3 import IntegrityError
from config import DB_URI
from views import index
from flask import render_template, request, redirect, url_for, flash
from forms.formulario import CadastroVeiculoForm





# Configuração das rotas
def home():
    return render_template('index.html')


# Rota para exibir todos os veículos cadastrados
def obtertodos_veiculos():
    veiculos = CadastroVeiculo.query.all()
    return render_template('todos_veiculos.html', veiculos=veiculos)

# Rota para cadastrar veículo
def cadastrar_veiculo():
    form = CadastroVeiculoForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Dados do formulário são válidos
        imei = form.imei.data
        fabricante = form.fabricante.data
        modelo = form.modelo.data
        placa = form.placa.data
        quilometragem = form.quilometragem.data
        foto = form.foto.data
        ano_fabricacao = form.ano_fabricacao.data
        cor = form.cor.data
        tipo_combustivel = form.tipo_combustivel.data
        crvl_ano = form.crvl_ano.data
        secretaria = form.secretaria.data

        # Verificar se o IMEI já existe
        veiculo_existente = CadastroVeiculo.query.filter_by(imei=imei).first()
        if veiculo_existente:
            flash('IMEI já existe. Por favor, insira um IMEI único.', 'error')
            return redirect(url_for('cadastrar_veiculo_route'))

        # Criar uma nova instância de CadastroVeiculo
        novo_veiculo = CadastroVeiculo(
            imei=imei,
            fabricante=fabricante,
            modelo=modelo,
            placa=placa,
            quilometragem=quilometragem,
            foto=foto,
            ano_fabricacao=ano_fabricacao,
            cor=cor,
            tipo_combustivel=tipo_combustivel,
            crvl_ano=crvl_ano,
            secretaria=secretaria
        )

        # Adicionar o novo veículo ao banco de dados
        db.session.add(novo_veiculo)
        # Confirmar a transação no banco de dados
        db.session.commit()

        flash('Veículo cadastrado com sucesso!', 'success')
        return redirect(url_for('obtertodos_veiculos_route'))

    return render_template('cadastro_veiculo.html', form=form)





# Rota para editar um veículo existente
def editar_veiculo(id):
    # Obtém o veículo pelo ID fornecido
    veiculo = CadastroVeiculo.query.get(id)
    if request.method == 'POST':
        # Obtém os dados do formulário enviado pelo método POST
        imei = request.form['imei']
        fabricante = request.form['fabricante']
        modelo = request.form['modelo']
        placa = request.form['placa']

        # Verifica se o campo quilometragem foi preenchido
        quilometragem_str = request.form['quilometragem']
        quilometragem = float(quilometragem_str) if quilometragem_str else None

        foto = request.form['foto']
        ano_fabricacao = int(request.form['ano_fabricacao'])
        cor = request.form['cor']
        tipo_combustivel = request.form['tipo_combustivel']
        crvl_ano = int(request.form['crvl_ano'])
        secretaria = request.form['secretaria']
        # Verifica se o novo IMEI já existe (ignorando o veículo atual)
        veiculo_existente = CadastroVeiculo.query.filter(CadastroVeiculo.imei == novo_imei, CadastroVeiculo.id != id).first()
        if veiculo_existente:
            flash('IMEI já existe. Por favor, insira um IMEI único.', 'error')
            return redirect(url_for('editar_veiculo_route', id=id))
        # Atualiza os dados do veículo com os dados do formulário enviado pelo método POST
        veiculo.imei = novo_imei
        veiculo.placa = novo_placa
        try:
            # Confirma a transação no banco de dados
            db.session.commit()
        except IntegrityError:
            # Se ocorrer um erro de integridade (IMEI duplicado), faça o rollback e exiba uma mensagem de erro
            db.session.rollback()
            flash('Erro ao editar veículo. Por favor, insira um IMEI único.', 'error')
            return redirect(url_for('editar_veiculo', id=id))
        # Redireciona para a rota que exibe todos os veículos
        return redirect(url_for('obtertodos_veiculos_route'))
    # Renderiza o template 'edit_veiculo.html' para edição de dados
    return render_template('editar_veiculo.html', veiculo=veiculo)


# Rota para deletar um veículo existente
def deletar_veiculo(id):
    veiculo = CadastroVeiculo.query.get(id)
    db.session.delete(veiculo)
    db.session.commit()
    return redirect(url_for('obtertodos_veiculos_route'))




# Executa o aplicativo se este script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
