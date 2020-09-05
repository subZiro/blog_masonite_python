"""User Model."""

from config.database import Model


class User(Model):
    """User Model."""

    __fillable__ = ['name', 'email', 'password', 'avatar', 'status']

    __auth__ = 'email'
