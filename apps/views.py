from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib import messages
from django.forms import modelformset_factory
from django.views.decorators.http import require_POST
from django.apps import apps

from apps.forms import CommentForm, PostForm, MediaForm
from .models import Comment, Media, Post


# Create your views here.

<<<<<<< HEAD

@login_required
def create_post(request: HttpRequest) -> HttpResponse:
    template_name: str = 'apps/post/create.html'
    context: dict[str, any] = {}
    mediaFormset = modelformset_factory(model=Media, form=MediaForm, extra=2)
    if request.method == 'POST':
        form_text = PostForm(data=request.POST)
        form_media = mediaFormset(request.POST, request.FILES)
        text = form_text.data
        media = form_media.data

        if bool(text) or bool(media):
            if all([form_text.is_valid(), form_media.is_valid()]):
                print(form_media.data, form_text.data)
                pub = form_text.save(commit=False)
                pub.owner = request.user
                pub.save()

                if request.FILES:
                    # for file in request.FILES.getlist('image'):
                    # 	Media.objects.create(post=pub, image=file)
                    new_media = form_media.save(commit=False)
                    for f in new_media:
                        f.post = pub 
                        f.save()
                    messages.success(request, 'Post was added success')
                return redirect('post_list')
            else:
                form_text = PostForm()
                form_media = mediaFormset(queryset=Media.objects.none())
                messages.error(request, "Oups, pls try later")
        else:
            form_text = PostForm()
            form_media = mediaFormset(queryset=Media.objects.none())
            messages.error(request, "Oups, pls populate these fields")
    else:
        form_text = PostForm()
        form_media = mediaFormset(queryset=Media.objects.none())
    context['form_text'] = form_text
    context['form_media'] = form_media
    return render(request, template_name, context)


@login_required
def update_post(request: HttpRequest, post_id: int) -> HttpResponse:
    template_name: str = 'apps/post/create.html'
    context: dict[str, any] = {}
    post = get_object_or_404(Post, pk=post_id)
    media = post.post_media.all()
    mediaFormset = modelformset_factory(model=Media, form=MediaForm, extra=2, can_delete=True)
    if request.method == 'POST':
        form_text = PostForm(data=request.POST, instance=post)
        form_media = mediaFormset(request.POST, request.FILES)
        text = form_text.data
        media = form_media.data

        if bool(text) or bool(media):
            if all([form_text.is_valid(), form_media.is_valid()]):
                print(form_media.data, form_text.data)
                pub = form_text.save(commit=False)
                pub.owner = request.user
                pub.save()

                if request.FILES:
                    # for file in request.FILES.getlist('image'):
                    # 	Media.objects.create(post=pub, image=file)
                    new_media = form_media.save(commit=False)
                    for f in new_media:
                        f.post = pub 
                        f.save()
                    messages.success(request, 'Post was added success')
                return redirect('post_list')
            else:
                form_text = PostForm(instance=post)
                form_media = mediaFormset(queryset=media)
                messages.error(request, "Oups, pls try later")
        else:
            form_text = PostForm(instance=post)
            form_media = mediaFormset(queryset=media)
            messages.error(request, "Oups, pls populate these fields")
    else:
        form_text = PostForm(instance=post)
        form_media = mediaFormset(queryset=media)
    context['form_text'] = form_text
    context['form_media'] = form_media
    return render(request, template_name, context)


@login_required
def post_list(request: HttpRequest) -> HttpResponse:
    template_name: str = 'apps/post/list.html'
    context: dict[str, any] = {}
    posts = Post.objects.select_related('owner')\
        .prefetch_related('users_like').all()
    context['posts'] = posts
    return render(request, template_name, context)


@login_required
def add_comment(request: HttpRequest, post_id: int) ->  HttpResponse:
    template_name: str = 'apps/comment/form.html'
    context: dict[str, any] = {}
    post = get_object_or_404(Post.objects\
         .select_related('owner')\
        .prefetch_related('users_like').all(), pk=post_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid() and post:
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.post = post
            new_form.save()
            messages.success(request, 'Comment was added success')
            return redirect('post_list')
        else:
            form = CommentForm()
            messages.error(request, "Oups, pls try later")
    else:
        form = CommentForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def update_comment(request: HttpRequest, post_id: int, id: int) ->  HttpResponse:
    
    template_name: str = 'apps/comment/form.html'
    context: dict[str, any] = {}
    post = get_object_or_404(Post.objects\
         .select_related('owner')\
        .prefetch_related('users_like').all(), pk=post_id)
    comment = get_object_or_404(Comment, pk=id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid() and post:
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.post = post
            new_form.save()
            messages.success(request, 'Comment was added success')
            return redirect('post_list')
        else:
            form = CommentForm(instance=comment)
            messages.error(request, "Oups, pls try later")
    else:
        form = CommentForm(instance=comment)
    context['form'] = form
    context['comment'] = comment
    return render(request, template_name, context)


@login_required
@require_POST
def like_item(request):
    action = request.POST.get("action")
    item_id = request.POST.get('item_id')
    model = request.POST.get('model')
    item = apps.get_model('apps', model)
    print(item)
    if action and item_id:
        try:
            obj = item.objects.get(id=item_id)
            if action == 'like':
                obj.users_like.add(request.user)
            else:
                obj.users_like.remove(request.user)
            return JsonResponse({'status': 'success'})
        except item.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})
=======
>>>>>>> b9953a5 (remove venv and __pycahe__)
