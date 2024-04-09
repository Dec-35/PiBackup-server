from flask import Blueprint
import uuid

getId = Blueprint("getId", __name__)


@getId.route("/api/getId")
def index():
    id = uuid.uuid4()
    return {"id": str(id)}
