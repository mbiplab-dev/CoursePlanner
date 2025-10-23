from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return render_template("auth/login.html")

@auth_bp.route("/go-dashboard")
def go_dashboard():
    return redirect(url_for("dashboard.dashboard_home"))
