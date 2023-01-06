from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

def home_view(request):
    user_queryset = User.objects.all()
    context = {
        'object_list': user_queryset
    }
    return render(request, 'home-view.html', context)
