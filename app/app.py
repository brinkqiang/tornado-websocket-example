import os
from tornado import web
from tornado import ioloop
from tornado import websocket

clients = [] 

class IndexHandler(web.RequestHandler):
	@web.asynchronous
	def get(self):
		self.render("index.html")


class WebSocketHandler(websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
		if self not in clients:
			clients.append(self)

	def on_close(self):
		if self in clients:
			clients.remove(self)


if __name__ == '__main__':
	application = web.Application([
		(r'/',IndexHandler),
		(r'/ws',WebSocketHandler),
		],
		template_path = os.path.join(os.path.dirname(__file__),'templates'),
		static_path = os.path.join(os.path.dirname(__file__),'static'),
		debug=True)

	application.listen(7777)
	ioloop.IOLoop.instance().start()
