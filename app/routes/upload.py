from flask import Blueprint, request
import os
from werkzeug.utils import secure_filename


upload = Blueprint("upload", __name__)

upload = Blueprint("upload", __name__)


@upload.route("/api/upload", methods=["POST"])
def index():
    # Ensure the request is multipart/form-data
    if "multipart/form-data" not in request.headers.get("Content-Type"):
        return {"error": "Content-Type must be multipart/form-data"}

    # Get the id from the form data
    id = request.form.get("id")
    if id is None:
        return {"error": "No id provided"}

    backup_folder = os.path.join("backups", id)
    if not os.path.exists(backup_folder):
        # create the folder if it doesn't exist
        os.makedirs(backup_folder)

    files = request.files.getlist("photo")
    if len(files) == 0:
        return {"error": "No files provided"}

    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(backup_folder, filename))

    # get the latest file's date
    files = sorted(
        os.listdir(backup_folder),
        key=lambda f: os.path.getmtime(os.path.join(backup_folder, f)),
    )

    # If the directory is empty, return null
    if not files:
        return {"date": None, "error": "No files found"}

    # Get the last modified file's date
    last_modified_date = os.path.getmtime(os.path.join(backup_folder, files[-1]))

    # Return the last modified date
    return {"success": True, "date": last_modified_date}
