from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bac33467956c034b85718b84bbde214b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

#Class model for the user table in sqlite
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return self.username

#site routes 
@app.route('/')
def home():
    return 'hello world'

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        #create the bcrypt variable
        bcrypt = Bcrypt()
        #obtain the values submitted into the form
        passhash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        username = form.username.data
        email = form.email.data
        #create the user object to add into the db
        user = User(username=username, email=email, password=passhash)
        #add the user
        db.session.add(user)
        db.session.commit()
        #redirect the user back to the home page after logging in 
        
        flash(f'Account created for {form.username.data}')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
