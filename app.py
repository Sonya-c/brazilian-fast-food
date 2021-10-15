from flask import Flask, render_template,redirect,url_for,request
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_manager
from flask_login.utils import login_required

from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm,SignupForm



app = Flask(__name__)
app.config['SECRET_KEY']= '\x01\xe3i\x1c\xfc\x1c\xa3E\xc1%\xbfr\x9f\xd7\xdb\xc1\x11#t4\xec(\x8a\xed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager(app)
#login_manager.login_view = ""

# init SQLAlchemy 
db = SQLAlchemy(app)
from models import Employee, User


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
    return render_template('dashboard.html')

@app.route('/register')
@login_required
def register():
    print('session: '+str(current_user.is_authenticated))
    return render_template('register.html')

@app.route('/buscar')
@login_required
def buscar():
    print('session: '+str(current_user.is_authenticated))
    
    return render_template('buscarEmpleado.html', employeers = Employee.getAll())
    
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
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            
            login_user(user, remember=form.remember_me.data)
            print("login status: "+ str(current_user.is_authenticated)+" "+str(current_user.name))
            return redirect(url_for('dashboard'))
            #next_page = request.args.get('next')
            
            #if not next_page or url_parse(next_page).netloc != '':
            #    next_page = url_for('index')
            #return redirect(next_page)
    return render_template('login.html', form=form)

@app.route("/signup/", methods=["GET", "POST"])
@login_required
def show_signup_form():
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = SignupForm()
    
    #print(f"app.show_sign() MENSAJE {form.gender.data}")
    #print(f"app.show_signup_form MENSAJE {form.contract_start.data}")

    if form.validate_on_submit():
        print('app.show_sign() MENSAJE sending employee')

        employee = Employee(email = form.email_address,
            gender = form.gender,
            address = form.address,
            branch = form.branch,
            job = form.job_title,
            contract = form.contract,
            salary = form.salary,
            start = form.contract_start,
            end = form.contract_end)

        employee.save()
       
    return render_template("register.html", form=form)

#logout ------------------------------------
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)   