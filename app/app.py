import os
from tornado import web
from tornado import ioloop


class IndexHandler(web.RequestHandler):
	def get(self):
		self.render("index.html")

if __name__ == '__main__':
	application = web.Application([
		(r'/',IndexHandler)],
		template_path = os.path.join(os.path.dirname(__file__),'templates'),
		static_path = os.path.join(os.path.dirname(__file__),'static'),
		debug=True)

	application.listen(7777)
	ioloop.IOLoop.instance().start()
