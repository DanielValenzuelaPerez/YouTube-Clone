from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

from accounts.models import Account
from accounts.forms import AccountForm

def account_create_view(request):
    form = AccountForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        object = form.save()
        context['form'] = AccountForm()
    return render(request, 'accounts/create.html', context=context)
