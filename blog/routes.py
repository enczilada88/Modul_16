from blog import app
from flask import render_template, request, flash, session, redirect, url_for
from blog.models import Entry, db
from blog.forms import EntryForm
from blog.forms import *




@app.route('/')
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template('homepage.html', all_posts=all_posts)


@app.route('/new-post/', methods=['GET', 'POST'])
def create_entry():
    return create_entry()


@app.route('/edit-post/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id: int):
    return edit_entry(entry_id=entry_id)



#changes

def create_entry(**kwargs):
    # GET
    entry_id = kwargs.pop('entry_id', None)
    form = EntryForm()
    entry = None
    errors = None
    if entry_id:
        entry = Entry.query.filter_by(id=entry_id).first_or_404()
        form = EntryForm(obj=entry)

    # POST
    if request.method == 'POST':
        if form.validate_on_submit():
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
                db.session.commit()
                flash('Nowy post został dodany. '
                      'Aby wyświetlić go na stronie głównej pamiętaj aby zaznaczyć "Wpis opublikowany"')
        else:
            errors = form.errors
    return render_template('entry_form.html', form=form, errors=errors)





def edit_entry(**kwargs):
    # GET
    entry_id = kwargs.pop('entry_id', None)
    form = EntryForm()
    entry = None
    errors = None
    if entry_id:
        entry = Entry.query.filter_by(id=entry_id).first_or_404()
        form = EntryForm(obj=entry)

    # POST
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry_id:
                form.populate_obj(entry)
                db.session.commit()
                flash('Zmiany w poscie zostały zapisane. '
                      'Aby wyświetlić go na stronie głównej pamiętaj aby zaznaczyć "Wpis opublikowany"')
        else:
            errors = form.errors
    return render_template('entry_form.html', form=form, errors=errors)

    # POST
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry_id:
                form.populate_obj(entry)
                db.session.commit()
                flash('Zmiany w poscie zostały zapisane. '
                      'Aby wyświetlić go na stronie głównej pamiętaj aby zaznaczyć "Wpis opublikowany"')
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
                db.session.commit()
                flash('Nowy post został dodany. '
                      'Aby wyświetlić go na stronie głównej pamiętaj aby zaznaczyć "Wpis opublikowany"')
        else:
            errors = form.errors
    return render_template('entry_form.html', form=form, errors=errors)
