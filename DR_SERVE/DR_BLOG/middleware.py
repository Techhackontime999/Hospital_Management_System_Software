from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
allowed_paths = ['DRAppoint/Appointment/']

class XFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Define the URL path where you want to allow embedding
        allowed_paths = ['/DR_BLOG/', '/DRAppoint/']
        
        # Check if the request path matches any of the allowed paths
        if any(request.path.startswith(path) for path in allowed_paths):
            # Allow embedding only for these paths
            response['X-Frame-Options'] = 'ALLOWALL'  # or 'SAMEORIGIN' if it's on the same domain
        else:
            # Use the default X-Frame-Options setting (SAMEORIGIN) for other paths
            response['X-Frame-Options'] = getattr(settings, 'X_FRAME_OPTIONS', 'DENY')
        
        return response
