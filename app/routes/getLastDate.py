from flask import Blueprint, request
import os

getLastDate = Blueprint("getLastDate", __name__)


@getLastDate.route("/getLastDate")
def index():
    # Look in the backups folder for the folder with the provided id
    id = request.args.get("id")
    if id == None:
        return {"error": "No id provided"}

    backup_folder = os.path.join("./", "backups", id)
    if not os.path.exists(backup_folder):
        return {"date": "None", "error": "No backups found for the provided id"}

    files = sorted(
        os.listdir(backup_folder),
        key=lambda f: os.path.getmtime(os.path.join(backup_folder, f)),
    )

    # If the directory is empty, return null
    if not files:
        return {"date": None}

    # Get the last modified file's date
    last_modified_date = os.path.getmtime(os.path.join(backup_folder, files[-1]))

    # Return the last modified date
    return {"date": last_modified_date}
