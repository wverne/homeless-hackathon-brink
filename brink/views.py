import datetime
import pytz

from django.http import HttpResponseBadRequest
from django.shortcuts import render

from .models import HelpRequest


FORM_TYPE_MAP = {
    'rough-sleeping': HelpRequest.TYPE_ROUGH_SLEEPING,
    'begging': HelpRequest.TYPE_BEGGING,
    'asb': HelpRequest.TYPE_ANTISOCIAL_BEHAVIOR
}


def help_view(request):
    template_dict = {}

    if request.method == 'POST':
        try:
            report_type = FORM_TYPE_MAP[request.POST['report-type']]
        except KeyError:
            return HttpResponseBadRequest("no type found")

        help_request = HelpRequest.objects.create(
            time=datetime.datetime.now(tz=pytz.UTC),
            latitude=float(request.POST['latitude']),
            longitude=float(request.POST['longitude']),
            type=report_type
        )

        template_dict['message'] = 'Thank you!'

    return render(request, 'help.html', template_dict)
