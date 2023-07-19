from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["celine","joelle","Avigail", "George", "Fouad", "Gi"]


@app.route('/',methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method =='POST': 
		username1=request.form['username']
		password1=request.form['password']
		if password1 == password and username.lower()==username1.lower():
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')
    
@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template('friend_exists.html', n=name,facebook_friends=facebook_friends)    

@app.route('/home')  # '/' for the default page
def home():
  	return render_template('home.html',facebook_friends=facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)

