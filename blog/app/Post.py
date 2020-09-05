"""Post Model."""

from config.database import Model
from orator.orm import belongs_to


class Post(Model):
    """Post Model."""
    # __table__ = 'blog'
    __fillable__ = ['title', 'image', 'author_id', 'body']

    @belongs_to('author_id', 'id')
    def author(self):
        """

        :return: model
        """
        from app.User import User
        return User
