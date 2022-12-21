from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
# from flask_app.models import word
from flask_app.__init__ import app




class Score:
    def __init__(self, data):
        self.id = data['id']
        self.errors = data['errors']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = None
