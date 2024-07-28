# store/middleware.py

from datetime import datetime

class ActivityTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            print(f'User: {request.user.username}, Path: {request.path}, Time: {datetime.now()}')
        return response
