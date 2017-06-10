import os
import json
from tornado import web
from tornado import ioloop
from tornado import websocket
from tornado.options import options, define

import redis

r = redis.Redis("127.0.0.1", 6379)


define("port", default=8109, help="Default port", type=int)


node_id = "127.0.0.1:{}".format(options.port)


class WebSocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print("open a connection")

    def on_message(self, msg):
        self.write_message('response by {}:{}'.format(node_id, msg))

    def on_close(self):
        pass

if __name__ == '__main__':
        options.parse_command_line()
        application = web.Application([
        (r'/ws',WebSocketHandler),
        ],
        debug=True)

    application.listen(options.port)
    print 'Listen on ', options.port
    r.lpush("NODE_HOST_LIST","127.0.0.1:{}".format(options.port))
    """
    when the node has shutdown, should clean the node information by pop out ...
    so the node need to do some signal catch (i.e CTRL+C ) and then clean it ...
    """
    ioloop.IOLoop.instance().start()
