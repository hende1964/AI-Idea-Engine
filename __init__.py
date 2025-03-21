from flask import Flask
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Import your routes to register them with the app
from routes import main_routes
app.register_blueprint(main_routes)

# Optional: Hook up any additional extensions (e.g., databases, logging)
# from database import init_db
# init_db(app)
