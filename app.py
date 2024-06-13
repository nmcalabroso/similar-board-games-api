import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from lib.api.users import users, user

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Register blueprints
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
