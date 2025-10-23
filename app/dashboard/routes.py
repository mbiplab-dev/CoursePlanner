from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard_home():
    return render_template("dashboard/dashboard.html",
                           credits=24,
                           level="Level 3")
