from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional, Length, NumberRange

class CadastroVeiculoForm(FlaskForm):
    imei = StringField('IMEI', validators=[DataRequired(), Length(min=15, max=15)])
    fabricante = StringField('Fabricante', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    placa = StringField('Placa', validators=[DataRequired(), Length(min=7, max=7)])
    quilometragem = FloatField('Quilometragem', validators=[Optional(), NumberRange(min=0)])
    foto = StringField('Foto', validators=[Optional(), Length(max=255)])
    ano_fabricacao = IntegerField('Ano de Fabricação', validators=[Optional(), NumberRange(min=1900)])
    cor = StringField('Cor', validators=[DataRequired()])
    tipo_combustivel = SelectField('Tipo de Combustível', choices=[('gasolina', 'Gasolina'), ('alcool', 'Álcool'), ('diesel', 'Diesel')], validators=[DataRequired()])
    crvl_ano = IntegerField('Ano do CRVL', validators=[Optional(), NumberRange(min=1900)])
    secretaria = StringField('Secretaria', validators=[DataRequired()])
