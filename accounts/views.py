from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.models import Creator
from engagement.models import Subscription, ContentEngagement
from content.models import Content

User = get_user_model()


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account ({username}) successfuly created!")
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect.')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def channelPage(request, username=None):
    creator = None
    user = User.objects.filter(username=username).first()

    visiting_user = request.user
    subscribed = False
    if user:
        creator = Creator.objects.filter(user=user).first()
        if Subscription.objects.filter(user=visiting_user, creator=creator):
            subscribed = True
        videos = Content.objects.filter(creator=creator)
        context = {
            'user': user,
            'creator': creator,
            'subscribed': subscribed,
            'videos': videos
        }
        return render(request, 'accounts/channel.html', context=context)
    return redirect('home')


def become_content_creator(request, username):
    if request.method == 'POST':
        user = User.objects.filter(username=username).first()
        creator = Creator.objects.create(user=user)
        creator.save()
        context = {
            'user': user,
            'creator': creator
        }
        return redirect(f"/accounts/channel/{user.username}/", context)


def subscribe(request, username):
    if request.method == 'POST':
        user = User.objects.filter(username=username).first()
        creator = Creator.objects.filter(user=user).first()
        subscriber = User.objects.filter(id=request.user.id).first()
        create_subscription, created = Subscription.objects.get_or_create(user=subscriber, creator=creator)
        if not created:
            create_subscription.delete()
        context = {
            'user': user,
            'creator': creator,
            'subsribed': created
        }
        return redirect(f"/accounts/channel/{user.username}/", context)

def likes(request, username):
    user = User.objects.filter(username=username).first()
    likes = ContentEngagement.objects.filter(user=user, liked=True).values_list('content', flat=True)
    videos = Content.objects.filter(id__in=likes)
    context = {
        'videos': videos,
        'username': username
    }
    return render(request, 'accounts/likes.html', context=context)
