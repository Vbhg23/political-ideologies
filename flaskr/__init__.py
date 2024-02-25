from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config = True)

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    
    @app.route("/nazism")
    def display_nazism():
        return render_template("nazism.html")
    
    return app