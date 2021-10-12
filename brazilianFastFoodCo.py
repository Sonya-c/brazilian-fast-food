import os
from web_app import app

app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(debug=True)