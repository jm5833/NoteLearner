from flask import Flask, render_template
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bac33467956c034b85718b84bbde214b'
@app.route('/')
def home():
    return 'hello world'

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    return 'login page'
