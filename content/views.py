from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from accounts.models import Creator
from content.forms import ContentForm

User = get_user_model()


def upload(request):
    if not request.user.is_authenticated:
        return redirect('home')

    user = User.objects.get(username=request.user)
    creator = Creator.objects.get(user=user)
    form = ContentForm()
    context = {
        'form': form,
        'user': user,
        'creator': creator
    }
    if request.method == 'POST':
        form = ContentForm(request.POST)
        form.creator = creator
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.creator = creator
            new_video.save()
            messages.success(request, f"Video '{new_video.name}' uploaded successfuly")
            return redirect(f"/accounts/channel/{user.username}/", context)
        messages.error(request, 'There was an error uploading this video.')
    return render(request, 'content/upload.html', context=context)