# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('bp', __name__)

from . import home, user
