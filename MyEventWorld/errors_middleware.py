from MyEventWorld.core.validators.error_renders import *


class SimpleMiddleware:
    ERROR_400 = 400
    ERROR_403 = 403
    ERROR_404 = 404
    ERROR_500_and_above = 500

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == self.ERROR_400:
            return error_400(request)

        if response.status_code == self.ERROR_403:
            return error_403(request)

        if response.status_code == self.ERROR_404:
            return error_404(request)

        if response.status_code >= self.ERROR_500_and_above:
            return server_errors(request)

        return response
