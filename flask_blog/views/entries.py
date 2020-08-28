from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db

@app.route("/")
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')

@app.route("/new_entry")
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('new_entry'))
    return render_template('entries/new.html')

@app.route("/entries", methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )

    db.session.add(entry)
    db.session.commit()
    flash('新しい記事が投稿されました')
    return redirect(url_for('show_entries'))
