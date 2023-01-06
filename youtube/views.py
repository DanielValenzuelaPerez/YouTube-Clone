from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template.loader import render_to_string

User = get_user_model()

def home_view(request):
    user_queryset = User.objects.all()
    context = {
        'object_list': user_queryset
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING)
