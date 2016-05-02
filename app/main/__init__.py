# -*- coding:utf-8 -*-
from app import lm
from app.models import User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


from .index import main
from .auth import auth
from .user import user
from .book import book
from .comment import comment
from .log import log
