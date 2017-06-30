import datetime
import pytz

from django.shortcuts import render

from .models import HelpRequest


def help_view(request):
    template_dict = {}

    if request.method == 'POST':
        help_request = HelpRequest(
            time=datetime.datetime.now(tz=pytz.UTC),
            latitude=53.467,
            longitude=-2.233,
        )
        if 'help' in request.POST:
            help_request.type = HelpRequest.TYPE_ROUGH_SLEEPING
        elif 'safety' in request.POST:
            help_request.type = HelpRequest.TYPE_SAFETY
        elif 'health' in request.POST:
            help_request.type = HelpRequest.TYPE_HEALTH
        help_request.save()

        template_dict['message'] = 'Thank you!'

    return render(request, 'help.html', template_dict)
