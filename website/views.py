from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Create the blueprint variable
views = Blueprint('views', __name__)


@views.route('/')  # Create a route(URL) to the blueprint variable
@login_required
# Create a function that executes when the URL has been called
def home():
    # return "<h1>Test</h1>"
    return render_template("home.html")  # Returns a rendered html
