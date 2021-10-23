from flask import Flask, render_template,redirect,url_for,request
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_manager
from flask_login.utils import login_required

from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm,SignupForm


app = Flask(__name__)
app.config['SECRET_KEY']= '\x01\xe3i\x1c\xfc\x1c\xa3E\xc1%\xbfr\x9f\xd7\xdb\xc1\x11#t4\xec(\x8a\xed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager(app)
#login_manager.login_view = ""

# init SQLAlchemy 
db = SQLAlchemy(app)
from models import Employee, Performance, User

#global vars---
display_employee="none"
display_emp="none"
@app.context_processor
def employee_vars():
    global display_employee, display_emp
    try:
        if current_user.is_admin==True:
            display_employee='block'
            display_emp='none'

    except:
        display_employee='none'
        display_emp='block'
    return dict(em_display=display_employee, emp_display=display_emp)



# -------------- ROUTERS --------------------
@login_manager.user_loader
def load_user(user_id):   
    return User.get_by_id(int(user_id))

@app.route('/',methods=['GET','POST'])
def index():
    return redirect(url_for('login'))

@app.route('/dash')
@login_required
def dashboard():
    print(str(current_user.is_admin))
    return render_template('dashboard.html',value="none")

@app.route('/performance')
@login_required
def performance():
    return render_template('performance.html', employee = Performance.get_performance(current_user.email))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', employee = Employee.getEmployee(current_user.email))

@app.route('/buscar',methods=['GET', 'POST'])
@login_required
def buscar():
    if current_user.is_admin==True:

        if request.method == 'POST':
            User.delete_user(request.form['delete_email'])
            Employee.delete_employee(request.form['delete_email'])
            return "Usuario Eliminado Exitosamente!"
        else:
            form=SignupForm()
            return render_template('buscarEmpleado.html',form=form,employees = Employee.getAll(),numbers = len(Employee.getAll()))

    return 'ACCESO NO AUTORIZADO'

@app.route('/editar')
@login_required
def editar():
    return render_template('editarEmpleado.html')

# ---------------- login sentences ----------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = User.get_by_id(0)
    print(f"app.login() MENSAJE User: {user}")

    if user is  None:
        user = User(id=0,name='admin', email='admin',is_admin=True)
        user.set_password('admin')
        user.save()
    
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data.lower())
        if user is not None and user.check_password(form.password.data):
            
            login_user(user, remember=form.remember_me.data)
            print("login status: "+ str(current_user.is_authenticated)+" "+str(current_user.name))
            return redirect(url_for('dashboard'))
            #next_page = request.args.get('next')
            
            #if not next_page or url_parse(next_page).netloc != '':
            #    next_page = url_for('index')
            #return redirect(next_page)
    return render_template('login.html', form=form)

#--------------------CREAR EMPLEADO-------------------------------#

@app.route("/signup/", methods=["GET", "POST"])
@login_required
def show_signup_form():
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = SignupForm()
    
    #print(f"app.show_sign() MENSAJE {form.gender.data}")
    #print(f"app.show_signup_form MENSAJE {form.contract_start.data}")
    if form.is_submitted():
        print ("submitted")

    if form.validate():
        print ("valid")

    print(form.errors)

    if form.validate_on_submit():
        # print('error: ',form.errors)
        # print ('OK')
        # list_form = [form.email_address,form.gender.data,form.address.data,form.branch.data,form.job_title.data
        # ,form.contract.data,form.salary.data]
        user = User.get_by_email(form.email_address.data)
        if user is None:
            employee = Employee(
                name=form.name.data,
                lastname=form.lastname.data,
                email = form.email_address.data.lower(),
                employee_id = form.employee_id.data,
                gender = form.gender.data,
                address = form.address.data,
                branch = form.branch.data,
                job = form.job_title.data,
                contract = form.contract.data,
                salary = 56465,#form.salary.data,
                start = form.contract_start.data,
                end = form.contract_end.data)
            employee.save()
            user = User(name=form.name.data, email=form.email_address.data,is_admin=False)
            user.set_password(form.password1.data)
            user.save()
            
    if current_user.is_admin==True:
        return render_template("register.html", form=form)
    return "ACCESO NO AUTORIZADO"

#logout ------------------------------------
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)   