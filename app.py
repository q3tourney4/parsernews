from threading import Timer

from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from parsernews.projectnews.api.resources import get_posts
from parsernews.projectnews.parcing.hacker_news_parser import parcing_hackernew


class ServerJson(object):
    @Request.application
    def application(self, request):
        dispatcher["posts"] = get_posts
        response = JSONRPCResponseManager.handle(request.data, dispatcher)
        return Response(response.json, mimetype="application/json")

    def main(self):
        run_simple("0.0.0.0", 8000, self.application)


class PerpetualTimer:
    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


if __name__ == "__main__":

    # Каждые 10 минут новостные данные обновляются
    t = PerpetualTimer(600, parcing_hackernew)
    t.start()

    ServerJson().main()
