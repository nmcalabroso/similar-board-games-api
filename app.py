from flask import Flask
from lib.api.users import users, user

app = Flask(__name__)

# Register blueprints
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
