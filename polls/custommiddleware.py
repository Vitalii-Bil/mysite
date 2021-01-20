from .models import Log


class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class LogMiddleware(BaseMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/admin/'):
            return None
        else:
            log = Log()
            log.path = request.path
            log.method = request.method
            log.save()
            return None
