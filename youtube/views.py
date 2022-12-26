from django.http import HttpResponse
from django.template.loader import render_to_string

from accounts.models import Account

def home_view(request):
    account_queryset = Account.objects.all()
    context = {
        'object_list': account_queryset
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING)
