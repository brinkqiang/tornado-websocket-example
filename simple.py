import os
import json
from tornado import web
from tornado import ioloop
from tornado import websocket


class WebSocketHandler(websocket.WebSocketHandler):
        def check_origin(self, origin):
                return True

        def open(self):
            pass

        def on_message(self, msg):
            self.write_message('response :{}'.format(msg))

        def on_close(self):
            pass

if __name__ == '__main__':
        application = web.Application([
                (r'/ws',WebSocketHandler),
                ],
                debug=True)
        print 'Listen on 7788'
        application.listen(7788)
        ioloop.IOLoop.instance().start()
