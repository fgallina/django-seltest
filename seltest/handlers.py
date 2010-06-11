from django.core.servers.basehttp import WSGIRequestHandler

class SilentWSGIRequestHandler(WSGIRequestHandler):

    def log_message(self, format, *args):
        pass
