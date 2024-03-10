from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config = True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    
    @app.route("/spisok")
    def display_spisok():
        return render_template("spisok.html")

    @app.route("/nazism")
    def display_nazism():
        return render_template("nazism.html")
    
    @app.route("/communism")
    def display_communism():
        return render_template("communism.html")
    
    @app.route("/anarchism")
    def display_anarchism():
        return render_template("anarchism.html")

    @app.route("/monarchism")
    def display_monarchism():
        return render_template("monarchism.html")
    
    @app.route("/liberalism")
    def display_liberalism():
        return render_template("liberalism.html")
    
    return app