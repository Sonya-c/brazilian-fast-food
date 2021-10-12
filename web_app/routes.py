from flask import render_template
#from web_app.forms import RegisterForm
from web_app import app
from core.models import item_Collection

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/market')
def market():
    items = item_Collection
    return render_template('market.html', title='Market', items = items)
'''

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
'''