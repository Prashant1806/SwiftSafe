from flask import Flask, render_template

# create the Flask application instance
app = Flask(__name__)

# load the configuration file
app.config.from_object('config')

# import the routes
from app.auth.routes import auth_bp
from app.bot.routes import bot_bp

# register the blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(bot_bp)

# define a custom error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# define a custom error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
