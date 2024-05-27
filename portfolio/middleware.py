from django.utils.deprecation import MiddlewareMixin
from .models import VisitorCount


class UniqueVisitorCountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/":  # Chemin de la page d'accueil
            if not request.session.get("has_visited"):
                visitor_count, created = VisitorCount.objects.get_or_create(pk=1)
                visitor_count.count += 1
                visitor_count.save()
                request.session["has_visited"] = True
