from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from flaskr.auth import login_required

from flaskr.models import User, PoetryWallTable
from flaskr.db import db
from datetime import datetime

bp = Blueprint('poetrywall', __name__)

@bp.route('/')
def index():
    return render_template('poetrywall/index.html')

@bp.route('/wall', methods=('GET', 'POST'))
@login_required
def wall():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM poetrywall p JOIN user u ON p.author_id = u.id WHERE author_id = ?'
    #     ' ORDER BY created DESC',
    #     (g.user['id'],)
    # ).fetchall()
    posts = PoetryWallTable.query.filter_by(author_id=g.user.id).order_by(PoetryWallTable.created.desc()).all()
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'
        
        if not body:
            error = 'Body is required.'
        
        if error is not None:
            flash(error)
        else:
            # db = get_db()
            # db.execute(
            #     'INSERT INTO poetrywall (title, body, author_id)'
            #     ' VALUES (?, ?, ?)',
            #     (title, body, g.user['id'])
            # )
            # db.commit()

            new_post = PoetryWallTable(title=title, body=body, created=datetime.now(), author_id=g.user.id)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('poetrywall.wall'))

    return render_template('poetrywall/wall.html', posts=posts)

def get_post(post_id, check_author=True):
    # post = get_db().execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM poetrywall p JOIN user u ON p.author_id = u.id'
    #     ' WHERE p.id = ?',
    #     (post_id,)
    # ).fetchone()
    # post = PoetryWall.query.join(User).filter(PoetryWall.id == post_id).first()
    post = PoetryWallTable.query.join(User).add_columns(
        PoetryWallTable.id, PoetryWallTable.title, PoetryWallTable.body, PoetryWallTable.created,
        PoetryWallTable.author_id, User.username
    ).filter(PoetryWallTable.id == post_id).first()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(post_id))
    
    if check_author and post.author_id != g.user.id:
        abort(403)
    
    return post


@bp.route('/<int:post_id>/update', methods=('GET', 'POST'))
@login_required
def update(post_id):
    post = get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if not body:
            error = 'Body is required.'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            # db.execute(
            #     'UPDATE poetrywall SET title = ?, body = ?'
            #     ' WHERE id = ?',
            #     (title, body, post_id)
            # )
            # db.commit()
            post.title = title
            post.body = body
            db.session.commit()
            return redirect(url_for('poetrywall.wall'))
        
    return render_template('poetrywall/update.html', post=post)

@bp.route('/<int:post_id>/delete', methods=('POST',))
@login_required
def delete(post_id):
    post = get_post(post_id)
    # db = get_db()
    # db.execute('DELETE FROM poetrywall WHERE id = ?', (post_id,))
    # db.commit()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('poetrywall.wall'))