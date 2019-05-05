from flask_wtf import Form
from wtforms import StringField, Label
from wtforms.validators import DataRequired

class ConverterForm(Form):
    arab_num = StringField('arabic', validators = [DataRequired()])


