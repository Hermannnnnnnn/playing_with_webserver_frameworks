from flask import Flask

def create_app(testing: bool = True):
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return f'Hello, World! This is stupid. Testing {testing}'
    
    return app