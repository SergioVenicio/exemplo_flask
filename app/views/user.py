# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for
from .home import bp
from .. import db
from ..models import User


@bp.route('/users/')
@bp.route('/users/<int:id>/')
def list_users(id=None):
    get = request.args.get
    page = get('page', 1, type=int)
    search = get('search')
    args, kwargs = (), {}
    if id:
        kwargs.update({User.id: id})
    else:
        if search:
            args += (User.name.like('%'+search+'%'),)
    paginator = User.query.filter(*args, **kwargs).paginate(
        page, per_page=5, error_out=False)
    user = paginator.items
    return render_template(
        'user/list.html', user=user, paginator=paginator, search=search)


@bp.route('/user/add/', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        name  = request.form['name']
        email = request.form['email']
        if name and email:
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
    return render_template('user/add.html')


@bp.route('/user/edit/<int:id>/', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            user.name = name
            user.email = email
            db.session.add(user)
            db.session.commit()
    return render_template('user/add.html', user=user)


@bp.route('/user/remove/<int:id>/', methods=['POST'])
def remove_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    return redirect(url_for('bp.list_users'))
