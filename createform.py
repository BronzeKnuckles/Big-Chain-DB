from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class createform(FlaskForm):
	vehiclenumber = StringField('Vehicle_Number',validators = [DataRequired()])
	manufacturer = StringField('Manufacturer',validators = [DataRequired()])
	submit = SubmitField('Create Asset')