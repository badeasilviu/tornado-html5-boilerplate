from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class HomeHandler(BaseHandler):
    def get(self):
        self.render("base.html")
