from flask import render_template
from web_app.forms import EditForm, LoginForm, RegisterForm
from web_app import app
from core.models import get_available_branches, item_Collection, dummy_Employee, get_available_jobs

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    form = LoginForm()
    return render_template('login.html', form =form)

'''
@app.route('/market')
def market():
    items = item_Collection
    return render_template('market.html', title='Market', items = items)
'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # TO-DO: replace with database logic later on fetching corresponding employee(user).
    employee = dummy_Employee
    form = EditForm()
    form.job_title.choices = get_available_jobs()
    form.branch.choices = get_available_branches()
    form.address.data = employee['address']
    form.branch.data = employee['branch']
    form.contract.data = employee['contract']
    form.job_title.data = employee['job_title']
    form.salary.data = employee['salary']
    form.contract_start.data = employee['contract_start']
    form.contract_end.data = employee['contract_end']
    return render_template('edit.html', form=form, employee=employee)