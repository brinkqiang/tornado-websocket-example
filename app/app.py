import os
import json
from tornado import web
from tornado import ioloop
from tornado import websocket

clients = [] 

class DataSample:
    def __init__(self,name, country):
        self.name = name
        self.country = country



class IndexHandler(web.RequestHandler):
	@web.asynchronous
	def get(self):
		self.render("index.html")

class TableHandler(web.RequestHandler):
        def get(self):
            
            self.render("table.html")

class WebSocketHandler(websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
		if self not in clients:
			clients.append(self)

	def on_close(self):
		if self in clients:
			clients.remove(self)

class ApiHandler(web.RequestHandler):
	def get(self):
		name = self.get_argument('name')
		age = self.get_argument('age')
		data = {"name":name,"age":age}
		print 'data',data
		data = json.dumps(data)
		for c in clients:
			c.write_message(data)	
		self.write(data)

if __name__ == '__main__':
	application = web.Application([
		(r'/',IndexHandler),
		(r'/ws',WebSocketHandler),
		(r'/api',ApiHandler),
		(r'/table',TableHandler),
		],
		template_path = os.path.join(os.path.dirname(__file__),'templates'),
		static_path = os.path.join(os.path.dirname(__file__),'static'),
		debug=True)
        print 'Listen on 7777'
	application.listen(7777)
	ioloop.IOLoop.instance().start()
