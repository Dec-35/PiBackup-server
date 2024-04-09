from flask import Blueprint, request, send_file
import os

getImage = Blueprint("getImage", __name__)


@getImage.route("/api/getImage/<filename>")
def index(filename):
    id = request.args.get("id")

    if id is None:
        return "Please provide an id", 400

    # check if the folder exists
    if not os.path.exists(f"../backups/{id}"):
        return "User has no backups", 404

    # check if the file exists
    if not os.path.exists(f"../backups/{id}/{filename}"):
        return "File not found", 404

    # return the image
    return send_file(f"../backups/{id}/{filename}")
