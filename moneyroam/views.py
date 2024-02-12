from django.shortcuts import render
from django.views.generic.base import TemplateView


class StartingPageView(TemplateView):
    template_name = "starting_page.html"