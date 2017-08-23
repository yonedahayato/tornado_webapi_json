import tornado.ioloop
import tornado.web

class  MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("self.request.path: {}".format(self.request.path))

        print("self.get_argument('type'): {}".format(self.get_argument("type")))
        print("self.get_argument('start'): {}".format(self.get_argument("start")))
        print("self.get_argument('end'): {}".format(self.get_argument("end")))
        print("self.request.arguments: {}".format(self.request.arguments))

        self.write("Helloworld, "*100)
        self.write("<br>good by")

application = tornado.web.Application([
    (r"/api", MainHandler)
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()
