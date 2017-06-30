from django.shortcuts import render


def help_request_list_view(request):
    return render(request, 'help_request_list_view.html')
