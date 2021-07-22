from blog import app
from flask import render_template, request, flash, session, redirect, url_for
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
from blog.function import *


@app.route('/')
def index():
    return homepage()

@app.route('/new-post/', methods=['GET', 'POST'])
def create_entry():
    return create_post()


@app.route('/edit-post/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id: int):
    return edit_post(entry_id=entry_id)


@app.route('/delete/<int:entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id: int):
    return delete_post(entry_id=entry_id)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True
            flash('You are logged in', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template('login_form.html', form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('You are now logged out.', 'succcess')
    return redirect(url_for('index'))


@app.route('/drafts/', methods=['GET'])
@login_required
def list_drafts():
    return create_drafts()




