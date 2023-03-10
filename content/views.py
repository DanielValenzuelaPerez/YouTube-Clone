from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from accounts.models import Creator
from content.forms import ContentForm, PlaylistForm
from content.models import Content, PlaylistContent
from engagement.models import ContentEngagement, ContentComment
from engagement.forms import ContentCommentForm

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
            messages.success(request, f"Video '{new_video.name}' uploaded successfuly.")
            return redirect(f"/accounts/channel/{user.username}/", context)
        messages.error(request, 'There was an error uploading this video.')
    return render(request, 'content/upload.html', context=context)


def video(request, id):
    try:
        video = Content.objects.get(id=id)
    except Content.DoesNotExist:
        messages.error(request, f"Video doesn't exist.")
        return redirect(request, 'home')
    creator = Creator.objects.get(id=video.creator.id)
    user = User.objects.get(id=creator.user.id)
    form = ContentCommentForm()
    context = {
        'form': form,
        'playlist_form': PlaylistForm(),
        'video': video,
        'channel': user.username
    }
    # Comment
    if request.method == 'POST':
        form = ContentCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content = video
            new_comment.user = request.user
            new_comment.reply_to = _get_reply_to(request)
            form.save()
    return render(request, 'content/video.html', context)

def _get_reply_to(request):
    # https://youtu.be/KrGQ2Nrz4Dc
    parent_obj = None
    try:
        parent_id = int(request.POST.get('reply_to'))
    except:
        parent_id = None
    if parent_id:
        parent_qs = ContentComment.objects.filter(id=parent_id)
        if parent_qs.exists():
            parent_obj = parent_qs.first()
    return parent_obj

def like(request, id):
    if request.method == 'POST':
        video = Content.objects.get(id=id)
        user = User.objects.get(id=request.user.id)
        # todo error check for unaunthenticated user
        creator = Creator.objects.get(id=video.creator.id)
        channel = User.objects.get(id=creator.user.id).username

        engagement, created = ContentEngagement.objects.get_or_create(content=video, user=user)
        if created:
            engagement.liked = True
        else:
            if engagement.liked is True:
                engagement.liked = None
            else:
                engagement.liked = True
        engagement.save()
        video.get_likes_dislikes_count()
        
        context = {
            'video': video,
            'channel': channel
        }
        return redirect(f"/content/video/{id}", context)

def dislike(request, id):
    if request.method == 'POST':
        video = Content.objects.get(id=id)
        user = User.objects.get(id=request.user.id)
        # todo error check for unaunthenticated user
        creator = Creator.objects.get(id=video.creator.id)
        channel = User.objects.get(id=creator.user.id).username

        engagement, created = ContentEngagement.objects.get_or_create(content=video, user=user)
        if created:
            engagement.liked = False
        else:
            if engagement.liked is False:
                engagement.liked = None
            else:
                engagement.liked = False
        engagement.save()
        
        context = {
            'video': video,
            'channel': channel
        }
        return redirect(f"/content/video/{id}", context)

def create_playlist(request, id):
    try:
        video = Content.objects.get(id=id)
    except Content.DoesNotExist:
        messages.error(request, f"Video doesn't exist.")
        return redirect(request, 'home')
    creator = Creator.objects.get(id=video.creator.id)
    creator_user = User.objects.get(id=creator.user.id)
    context = {
        'form': ContentCommentForm(),
        'playlist_form': PlaylistForm(),
        'video': video,
        'channel': creator_user.username
    }
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            playlist.user = user
            playlist.save()
            print(playlist)
            playlist_content = PlaylistContent(playlist=playlist, content=video)
            playlist_content.save()
            print(playlist_content)
    return render(request, 'content/video.html', context)
    


