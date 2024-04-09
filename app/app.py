from flask import Flask
from routes import main_bp  # Import the Blueprint from routes.py

app = Flask(__name__)

# Register the Blueprint(s)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)
