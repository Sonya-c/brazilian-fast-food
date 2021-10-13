from flask import Flask, render_template,redirect,url_for,request
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_manager
from flask_login.utils import login_required
from werkzeug.urls import url_parse
from forms import LoginForm,SignupForm
from models import users,User,get_user


app = Flask(__name__)
app.config['SECRET_KEY']= 'AQUI VA LA CLAVE MAESTRA'
login_manager = LoginManager(app)
#login_manager.login_view = ""

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

# init SQLAlchemy so we can use it later in our models
#db = SQLAlchemy()

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

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
    return render_template('buscarEmpleado.html')
    
@app.route('/editar')
@login_required
def editar():
    return render_template('editarEmpleado.html')


#login sentences ----------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        print("pass: "+ form.password.data)
        print (user)
        if user is not None and user.check_password(form.password.data):
            
            login_user(user, remember=form.remember_me.data)
            print("login status: "+ str(current_user.is_authenticated))
            return redirect(url_for('dashboard'))
            #next_page = request.args.get('next')
            
            #if not next_page or url_parse(next_page).netloc != '':
            #    next_page = url_for('index')
            #return redirect(next_page)
    return render_template('login.html', form=form)


@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)

#logout ------------------------------------
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)   