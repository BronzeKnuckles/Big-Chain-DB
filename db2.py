from flask import Flask, render_template, url_for, redirect, flash
from backend import back
from createform import createform
from checkform import checkform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/create", methods=['GET','POST'])
def create():
	form = createform()
	if form.validate_on_submit():
		vehicle_number = form.vehiclenumber.data
		manufacturer1 = form.manufacturer.data
		signed_tx = back.docreate(vehicle_number,manufacturer1)
		flash(signed_tx)

	return render_template('create.html',form = form)

@app.route("/check", methods=['GET','POST'])
def check():
	form = checkform()
	if form.validate_on_submit():
		ID = form.id.data
		msg = back.checker(ID)
		flash(msg)

	return render_template('check.html',form = form)

@app.route("/transfer")
def transfer():
	return render_template('transfer.html')

@app.route("/query")
def query():
	return render_template('query.html')


if __name__=='__main__':
	app.run(debug=True)