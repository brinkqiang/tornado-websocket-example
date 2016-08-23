from tornado import web
from tornado import ioloop

class IndexHandler(web.RequestHandler):
	def get(self):
		self.write("Hello Tornado")

if __name__ == '__main__':
	application = web.Application([
			(r'/',IndexHandler)],
			debug=True)

	application.listen(7777)
	ioloop.IOLoop.instance().start()
