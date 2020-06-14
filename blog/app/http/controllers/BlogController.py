"""A BlogController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


from app.Post import Post


class BlogController(Controller):
    """BlogController Controller Class."""

    def __init__(self, request: Request):
        """BlogController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        # открытие страницы блога
        return view.render('blog')

    def store(self, request: Request):
        # New store Method
        Post.create(title=request.input('title'),
                    image='no img',
                    body=request.input('body'),
                    author_id=request.user().id
                    )

        return 'post created'
