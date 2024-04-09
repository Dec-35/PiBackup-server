from flask import Flask
from routes.getId import getId
from routes.getLastDate import getLastDate


app = Flask(__name__)

# Register Blueprints
app.register_blueprint(getId)
app.register_blueprint(getLastDate)


if __name__ == "__main__":
    app.run(debug=True)
