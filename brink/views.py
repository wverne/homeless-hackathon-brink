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

        gender = request.POST['gender']
        age = request.POST['age']
        clothing = request.POST['clothing']
        hair_colour = request.POST['hair']
        notes = ""

        if gender == 'unknown':
            notes += 'Gender unknown.'
        else:
            notes += 'Gender: {}.'.format(gender)

        if age == '':
            notes += ' Age unknown.'
        else:
            notes += ' Age estimate: {}.'.format(age)

        if clothing == '':
            notes += ' Clothing unknown.'
        else:
            notes += ' Clothing: "{}".'.format(clothing)

        if hair_colour == '':
            notes += ' Hair colour unknown.'
        else:
            notes += ' Hair colour: "{}".'.format(hair_colour)

        HelpRequest.objects.create(
            time=datetime.datetime.now(tz=pytz.UTC),
            latitude=float(request.POST['latitude']),
            longitude=float(request.POST['longitude']),
            type=report_type,
            notes=notes
        )

        template_dict['message'] = 'Thank you!'

    return render(request, 'help.html', template_dict)


def map_view(request):
    return render(request, "map.html", {
        'help_requests': HelpRequest.objects.filter(resolved=False).order_by('-time')[:20]
    })
