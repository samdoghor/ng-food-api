"""
## Module Name: editors.py

This module defines the EditorModel class, representing editors list.

"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .abc import BaseModel, MetaBaseModel
from utils import encode_auth_token

# model


class EditorModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines the Editor Model e.g Samuel, Doghor '''

    __tablename__ = 'editors'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    is_developer = db.Column(db.Boolean, default=False)
    contribution_point = db.Column(db.Integer, default=0, nullable=False)
    last_editor_login = db.Column(db.DateTime, default=datetime.utcnow)
    api_key = db.Column(db.String(), unique=True, nullable=True)
    secret_key = db.Column(db.String(), unique=True, nullable=True)
    salt = db.Column(db.String(), unique=True, nullable=True)

    is_approved = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def encode_token(self, id, first_name, last_name):
        return encode_auth_token(id, first_name, last_name)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'Editor(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email_address={self.email_address}, is_developer={self.is_developer}, last_editor_login={self.last_editor_login}, api_key={self.api_key}, secret_key={self.secret_key})'  # noqa
