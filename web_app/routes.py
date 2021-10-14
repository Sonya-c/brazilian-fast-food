import os
from flask import render_template, redirect,flash, url_for
from web_app.forms import EditForm, LoginForm, RegisterForm
from web_app import app
from core.models import get_available_branches, dummy_Employee, get_available_jobs
from core.utils import translate_gender


app.secret_key = os.urandom(24)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    form = LoginForm()
    return render_template('login.html', form =form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    form.job_title.choices = get_available_jobs()
    form.branch.choices = get_available_branches()

    if form.validate_on_submit():
        user_to_create = {
            'employee_id': form.employee_id.data, 
            'name' : form.name.data,
            'lastname' : form.lastname.data,
            'email_address' : form.email_address.data,
            'address' : form.address.data,
            'gender' : form.gender.data,
            'branch' : form.branch.data,
            'job_title' : form.job_title.data,
            'contract' : form.contract.data,
            'salary' : form.salary.data,
            'contract_start' : form.contract_start.data,
            'contract_end' : form.contract_end.data,
            'password_raw' : form.password1.data
        }
        print(user_to_create)
        
        return redirect(url_for('index'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Errores en los datos provistos: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # TO-DO: replace with database logic later on fetching corresponding employee(user). 
    
        form = EditForm()
        form.job_title.choices = get_available_jobs()
        form.branch.choices = get_available_branches()

        employee = dummy_Employee
        if form.validate_on_submit():
            employee['address'] = form.address.data
            employee['branch'] = form.branch.data
            employee['contract'] = form.contract.data
            employee['job_title'] = form.job_title.data
            employee['salary'] = form.salary.data
            employee['contract_start'] = form.contract_start.data
            employee['contract_end'] = form.contract_end.data
            print(employee)
            
            return redirect(url_for('index'))
        
        if form.errors != {}: #If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'Errores en los datos provistos: {err_msg}', category='danger')
        
        employee['gender'] = translate_gender(employee['gender'])
        form.address.data = employee['address']
        form.branch.data = employee['branch']
        form.contract.data = employee['contract']
        form.job_title.data = employee['job_title']
        form.salary.data = employee['salary']
        form.contract_start.data = employee['contract_start']
        form.contract_end.data = employee['contract_end']
        
        return render_template('edit.html', form=form, employee=employee)
    
    
    