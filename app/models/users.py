# -*- coding: utf-8 -*-

from ..extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))

    def __repr__(self):
        return '<User {}>'.format(self.name)
