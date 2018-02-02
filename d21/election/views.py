from django.shortcuts import render
from django.views.generic import TemplateView


class ElectionListView(TemplateView):  # TODO: make better base class
    template_name = 'index.html'
    # TODO: context


class ElectionDetailView(TemplateView):
    # TODO
    pass
