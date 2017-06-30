from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import HelpRequest


def help_request_list_view(request):
    help_requests = HelpRequest.objects.all()
    template = loader.get_template('help_request_list_view.html')

    context = {
        'help_requests': help_requests
    }

    response = template.render(context, request)

    return HttpResponse(response)
