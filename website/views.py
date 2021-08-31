from flask import Blueprint, render_template, request, flash
from flask.json import jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from . import db
from .models import Note
import json

# Create the blueprint variable
views = Blueprint('views', __name__)


# Create a route(URL) to the blueprint variable
@views.route('/', methods=['GET', 'POST'])
@login_required  # annot access this route if not login
# Create a function that executes when the URL has been called
def home():
    # return "<h1>Test</h1>"

    if request.method == 'POST':
        # data = request.form
        # print(data)
        note = request.form.get('note')
        if len(note) < 1:
            flash('The note is too short!', category='error')
        else:
            print(note, current_user.id)
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note has been added.', category='success')

    # Returns a rendered html
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('You have deleted a note!', category='success')

    return jsonify({})
