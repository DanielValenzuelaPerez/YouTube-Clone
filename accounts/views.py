from django.http import HttpResponse
from django.template.loader import render_to_string
from accounts.models import Account

def home_view(request):
    account = Account.objects.get(id=1)
    context = {
        'id': account.id,
        'handle': account.handle
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING)
