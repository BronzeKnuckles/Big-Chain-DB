from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
class checkform(FlaskForm):
	id = StringField('id',validators = [DataRequired()])
	submit = SubmitField('Create Asset')

