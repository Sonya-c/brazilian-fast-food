from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dash')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/editar')
def editar():
    return render_template('editarEmpleado.html')


if __name__ == '__main__':
    app.run()   