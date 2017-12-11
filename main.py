# -*- coding: utf-8 -*-
import os.path
from tornado import httpserver,ioloop,web
from tornado.options import define,options
import torndb
import tornado.options
from handlers import HANDLERS,TEMPLATE_PATH


define("port", default=8000, type=int)
define("mysql_host",default="127.0.0.1:3306",help="blog database host")
define("mysql_database",default="project",help="blog database name")
define("mysql_user",default="root",help="blog database user")
# define("mysql_password",default="",help="blog database password")


class Application(web.Application):
    def __init__(self):
        handlers = HANDLERS
        settings = dict(
          
            template_path = TEMPLATE_PATH,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
         
            xsrf_cookies = False,
            
            # cmd python：print base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)
            cookie_secret="tmxvMsfgRHqV61E6iZ/pJcVRAiHQZEmehIFLhNJtvYM=",
        )
        # Application
        web.Application.__init__(self,handlers,**settings)
        
        self.db = torndb.Connection(
            host= options.mysql_host,database=options.mysql_database,
            user= options.mysql_user,password=None)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
