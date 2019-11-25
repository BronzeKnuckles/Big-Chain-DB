from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class createform(FlaskForm):
    vehiclenumber = StringField('Vehicle_Number', validators=[DataRequired()])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    prikey = StringField('Private Key', validators=[DataRequired()])
    pubkey = StringField('Public Key', validators=[DataRequired()])
    submit = SubmitField('Create Asset')


class queryform(FlaskForm):
    search = StringField('keyword', validators=[DataRequired()])
    submit = SubmitField('Send query')


class transferform(FlaskForm):
    txid = StringField('transaction_id', validators=[DataRequired()])
    opk = StringField('owner_public_key', validators=[DataRequired()])
    rpk = StringField('recepient_public_key', validators=[DataRequired()])
    oprk = StringField('owner_private_key', validators=[DataRequired()])
    submit = SubmitField('Sign Transaction and Transfer')


class checkform(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    submit = SubmitField('Check for Asset')


class checkerpoform(FlaskForm):
    ID = StringField('id', validators=[DataRequired()])
    pk = StringField('public key', validators=[DataRequired()])
    submit = SubmitField('CHECK')


class initform(FlaskForm):
    submit = SubmitField('Generate Keypair')
