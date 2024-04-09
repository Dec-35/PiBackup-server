from flask import Flask
from routes.getId import getId  # Import the Blueprint from routes.py

app = Flask(__name__)

# Register the Blueprint(s)
app.register_blueprint(getId)

if __name__ == "__main__":
    app.run(debug=True)
