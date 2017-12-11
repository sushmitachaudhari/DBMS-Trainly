# -*- coding: utf-8 -*-
from views import *
import os.path

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
HANDLERS = [
    (r'/', MainHandler),
    (r'/login', LoginHandler),
    (r'/student', StudentHandler),
    (r'/admin', AdminHandler),
    (r'/staff', StaffHandler),
    (r'/register', RegisterHandler),
    (r'/registeres', RigisteresHandler),
    (r'/list', listHandler),
    (r'/listres', listresHandler),
    (r'/auth', AuthHandler),
    (r'/authres', AuthResHandler),
    (r'/catogres', CatogresHandler),
    (r'/enroll', EnrollHandler),
    (r'/enrollres', EnrollresHandler),
    (r'/ccomplete', CCompleteHandler),
    (r'/ccompletemid', CCompleteMidHandler),
    (r'/ccompleteres', CCompleteResHandler),
    (r'/certificate', CertificateHandler),
    (r'/certificateres', CertificateResHandler),
    (r'/historyres', HistoryResHandler)
]