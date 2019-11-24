from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class checkerpoform(FlaskForm):
	ID = StringField('id',validators = [DataRequired()])
	pk = StringField('public key', validators =[DataRequired()])
	submit = SubmitField('CHECK')
