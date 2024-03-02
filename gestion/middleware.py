# middleware.py
from django.urls import reverse
from django.http import HttpResponseRedirect

class NotFoundRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404 and not request.path.startswith('/admin/'):
            return HttpResponseRedirect(reverse('login'))  # Redirige a la página de inicio de sesión
        return response
