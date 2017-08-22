from flask import Flask
app = Flask(__name__)

# Blueprints
from app.nfe.controllers import nfe
# Register blueprints
app.register_blueprint(nfe, url_prefix='/nfe')

@app.route('/')
def hello_world():
    return 'Hello, World!'