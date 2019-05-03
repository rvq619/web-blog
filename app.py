from models.user import User


from flask import Flask, render_template, request, session



app = Flask(__name__) # '__main__'

@app.route('/') # www.mysite.com/api/
def hello_method():
	return render_template('login.html')

@app.route('/login')
def login_user():
	email = request.form['email']
	password = request.form['password']

	if User.login_valid(email, password):
		User.login(email)

	return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
	app.run() # run(port=4995) if port 5000 is taken


# https://translate.google.com/translate?hl=en&sl=ru&u=http://qaru.site/questions/13907130/does-initpy-have-to-be-in-every-directory-of-python-application&prev=search
# https://stackoverflow.com/questions/44642477/does-init-py-have-to-be-in-every-directory-of-python-application
# https://github.com/CrownStack/crownstack-playbook/wiki/Python-Flask-Playbook
