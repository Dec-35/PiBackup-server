from flask import Flask
from routes.getId import getId
from routes.getLastDate import getLastDate
from routes.home import home
from routes.upload import upload
from routes.getImages import getImages
from routes.getImage import getImage


app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home)
app.register_blueprint(getId)
app.register_blueprint(getLastDate)
app.register_blueprint(upload)
app.register_blueprint(getImages)
app.register_blueprint(getImage)

# use the static folder for css and js
app.static_folder = "../static"


if __name__ == "__main__":
    app.run(debug=True)
