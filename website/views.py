from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user

# Create the blueprint variable
views = Blueprint('views', __name__)


@views.route('/')  # Create a route(URL) to the blueprint variable
@login_required  # annot access this route if not login
# Create a function that executes when the URL has been called
def home():
    # return "<h1>Test</h1>"
    # Returns a rendered html
    return render_template("home.html", user=current_user)
