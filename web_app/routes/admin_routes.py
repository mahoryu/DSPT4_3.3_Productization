# web_app/routes/admin_routes.py

import os
from dotenv import load_dotenv

from flask import Blueprint, jsonify, request, flash, redirect #, render_template

from web_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

load_dotenv()
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")

API_KEY = ADMIN_API_KEY

# GET /admin/db/reset?api_key=abc123
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARMS", dict(request.args))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        return jsonify({"message": "DB RESET OK"})
    else:
        print("PERMISSIONG DENIED")
        flash("OOPS Permission Denied", "danger")
        return redirect("/")
