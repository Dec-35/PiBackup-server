from flask import Blueprint, request
import os

getImages = Blueprint("getImages", __name__)


@getImages.route("/api/getImages")
def index():
    id = request.args.get("id")

    if id is None:
        return "Please provide an id", 400

    # check if the folder exists
    if not os.path.exists(f"../backups/{id}"):
        return "User has no backups", 404

    # get the images from the folder
    images = os.listdir(f"../backups/{id}")
    if len(images) == 0:
        return "No images found", 404

    # return the images list
    return {"images": images}
