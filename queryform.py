from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
class queryform(FlaskForm):
	search = StringField('keyword',validators = [DataRequired()])
	submit = SubmitField('Send query')

