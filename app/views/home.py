# -*- coding: utf-8 -*-

from flask import render_template
from . import bp


@bp.route('/')
def home():
    return render_template('home/index.html')
