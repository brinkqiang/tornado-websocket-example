import os
import json
from tornado import web
from tornado import ioloop
from tornado import websocket
from tornado.options import options, define

define("port", default=8109, help="Default port", type=int)



class WebSocketHandler(websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
            print("open a connection")

        def on_message(self, msg):
            self.write_message('response :{}'.format(msg))

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
	ioloop.IOLoop.instance().start()
