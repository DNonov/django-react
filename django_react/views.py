import os
import logging
from django.http import HttpResponse
from django.views.generic import View


class FrontendAppView(View):
    """
    Serves the frontend react entry point.
    """

    index_file_path = os.path.join('build', 'index.html')

    def get(self, request):
        try:
            with open(self.index_file_path) as f:
                return HttpResponse(f.read())

        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have build the production
                version of the app. Visit http://localhost:3000/ instead after
                running 'npm start'.
                """,
                status=501,
            )