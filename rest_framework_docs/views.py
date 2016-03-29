from django.http import Http404
from django.views.generic.base import TemplateView

from .api_docs import ApiDocumentation
from .settings import drf_settings


class DRFDocsView(TemplateView):

    template_name = "rest_framework_docs/home.html"

    def get_context_data(self, **kwargs):
        if drf_settings["HIDE_DOCS"]:
            raise Http404("Django Rest Framework Docs are hidden. "
                          "Check your settings.")

        context = super(DRFDocsView, self).get_context_data(**kwargs)
        docs = ApiDocumentation()
        endpoints = docs.get_endpoints()

        query = self.request.GET.get("search", "")
        if query and endpoints:
            endpoints = [endpoint for endpoint in endpoints
                         if query in endpoint.path]

        context['query'] = query
        context['endpoints'] = endpoints
        context['base_template'] = drf_settings['TEMPLATE']
        return context
