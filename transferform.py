from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class transferform(FlaskForm):
	txid = StringField('transaction_id',validators = [DataRequired()])
	opk = StringField('owner_public_key',validators = [DataRequired()])
	rpk = StringField('recepient_public_key',validators = [DataRequired()])
	oprk = StringField('owner_private_key',validators = [DataRequired()])
	submit = SubmitField('TRANSFER')


