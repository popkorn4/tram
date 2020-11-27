from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField, IntegerField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class AddProduct(FlaskForm):
    name = TextField('name', validators = [Required()])
    category = TextField('category', validators = [Required()])
    photo_hash = TextField('photo')
    description = TextField('descr')
    submit = SubmitField('add')
    price =  TextField('price')
class login(FlaskForm):
    login = PasswordField('Login', validators = [Required()])
    submit = SubmitField('ENTER')
class order(FlaskForm):
    Name = TextField('Name', validators = [Required()])
    tel = TextField('Teleshone', validators = [Required()])
    adress = TextField('Adres', validators = [Required()])
    Maile = TextField('Maile', validators = [Required()])
    submit = SubmitField('Оформить заказ')