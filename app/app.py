from flask import Flask
from routes.getId import getId
from routes.getLastDate import getLastDate
from routes.home import home
from routes.upload import upload


app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home)
app.register_blueprint(getId)
app.register_blueprint(getLastDate)
app.register_blueprint(upload)


if __name__ == "__main__":
    app.run(debug=True)
