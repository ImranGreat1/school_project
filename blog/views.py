from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, MoreImages, MorePdfs, MoreVideos, Comment, Pdf_File
from .forms import *
from django.forms import modelformset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib import messages


def post_list(request):
    if request.user.is_authenticated:   
        user_dept = request.user.profile.department
        user_level = request.user.profile.level
        posts_list = Post.objects.filter(department=user_dept, level=user_level, status='publish')
    else:
        posts_list = Post.objects.published()

    q = request.GET.get('q')
    if q:
        posts_list = Post.objects.filter(
            Q(content__icontains=q) |
            Q(title__icontains=q) |
            Q(author__username__iexact=q)
        )

    paginator = Paginator(posts_list, 6)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7

    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'posts': posts,
        'page_range': page_range,
    }
    return render(request, 'blog/post_list.html', context)

@login_required
def favourite_posts(request):

    posts_list = Post.objects.filter(favourite=request.user.id)

    paginator = Paginator(posts_list, 4)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7

    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'posts': posts,
        'page_range': page_range,
    }
    return render(request, 'blog/post_list.html', context)



def proper_pagination(posts, index):

    start_index = 0
    end_index = 7

    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index

    return (start_index, end_index)

@login_required
def post_create(request):
    if not request.user.profile.is_representative():
        raise Http404
    if request.method == 'POST':
        form = PostCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.department = request.user.profile.department
            post.level = request.user.profile.level
            post.author = request.user
            post.save()

            return redirect(post.get_absolute_url())

    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/post_create.html', context)


def post_edit(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    if request.user != post.author:
        raise Http404()
    if request.method == 'POST':
        form = PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            pdf = form.cleaned_data.get('pdf')
            print(form.cleaned_data)
            form.save()

            return redirect(post.get_absolute_url())

    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
    }

    return render(request, 'blog/post_edit.html', context)



def add_image(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.author:
        raise Http404

    if request.method == 'POST':
        form = MoreImagesForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save(commit=False)
            image_obj.post = post
            image_obj.department = request.user.profile.department
            image_obj.level = request.user.profile.level
            image_obj.status = post.status
            image_obj.save()
            return redirect(post.get_absolute_url())
    else:
        form = MoreImagesForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_image.html', context)



def add_post_pdf(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.author:
        raise Http404
    if request.method == 'POST':
        form = MorePdfsForm(request.POST, request.FILES)
        pdf_obj = form.save(commit=False)
        pdf_obj.post = post
        pdf_obj.department = request.user.profile.department
        pdf_obj.level = request.user.profile.level
        pdf_obj.status = post.status
        pdf_obj.save()

        return redirect(post.get_absolute_url())

    else:
        form = MorePdfsForm()
    
    context = {
        'form': form,
    }

    return render(request, 'blog/add_pdf.html', context)



def edit_image(request, image_pk, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    image = get_object_or_404(MoreImages, pk=image_pk)
    if request.user != post.author:
        # return redirect(post.get_absolute_url())
        raise Http404()
    else:    
        if request.method == 'POST':
            form = MoreImagesEditForm(request.POST, request.FILES, instance=image)
            if form.is_valid():
                form.save()
                return redirect(post.get_absolute_url())

        else:
            form = MoreImagesEditForm(instance=image)
        
        context = {
            'form': form,
        }

        return render(request, 'blog/edit_image.html', context)


def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug, status='publish')
    is_liked = False
    is_favourite = False

    favourite = post.favourite.filter(id=request.user.id)
    if favourite.exists():
        is_favourite = True

    like = post.likes.filter(id=request.user.id)
    if like.exists():
        is_liked = True

    comments = Comment.objects.filter(post=post, reply=None)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                reply = Comment.objects.get(id=reply_id)
                comment = Comment(post=post, user=request.user, content=content, reply=reply)
            else:
                comment = Comment(post=post, user=request.user, content=content, reply=None)
            comment.save()
            return redirect(post.get_absolute_url())

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'is_liked': is_liked,
        'is_favourite': is_favourite,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }

    if request.is_ajax():
        html = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'blog/post_detail.html', context)



def delete_image(request, image_pk, post_pk):
    image = get_object_or_404(MoreImages, pk=image_pk)
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.author:
        raise Http404()
    image.delete()
    return redirect(post.get_absolute_url())



def pdf_delete(request, pk, post_pk):
    pdf = get_object_or_404(MorePdfs, pk=pk)
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.author:
        raise Http404()
    pdf.delete()
    return redirect(post.get_absolute_url())



@login_required
def like_post(request):
    if request.method == 'POST':

        id = request.POST.get('id')
        post = get_object_or_404(Post, id=id)
        is_liked = False

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user.id)
            is_liked = False
        else:
            post.likes.add(request.user.id)
            is_liked = True

        context = {
            'post': post,
            'is_liked': is_liked,
            'total_likes': post.total_likes(),
        }

    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})


def favourite(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)

        if post.favourite.filter(id=request.user.id).exists():
            post.favourite.remove(request.user.id)
            is_favourite = False
        else:
            post.favourite.add(request.user.id)
            is_favourite = True

        context = {
            'is_favourite': is_favourite,
            'post': post,
        }

        if request.is_ajax():
            html = render_to_string('blog/favourites.html', context, request=request)
            return JsonResponse({'form': html})


@login_required
def images_album(request):
    user_dept = request.user.profile.department
    user_level = request.user.profile.level
    published = 'publish'
    images_album = MoreImages.objects.filter(department=user_dept, level=user_level, status=published)
    context = {
        'images_album': images_album,
    }
    return render(request, 'blog/images_album.html', context)



def post_pdf_list(request):
    user_dept = request.user.profile.department
    user_level = request.user.profile.level
    pdf_list = MorePdfs.objects.filter(department=user_dept, level=user_level)
    context = {
        'pdf_list': pdf_list,
    }
    return render(request, 'blog/post_pdf_list.html', context)


def upload_pdf(request):
    if not request.user.profile.is_representative():
        raise Http404
    user_dept = request.user.profile.department
    user_level = request.user.profile.level
    if request.method == 'POST':
        form = PDF_UploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            pdf_obj = form.save(commit=False)
            pdf_obj.user = request.user
            pdf_obj.department = user_dept
            pdf_obj.level = user_level
            pdf_obj.save()
            return redirect('pdf_list')
    else:
        form = PDF_UploadForm()
    
    context = {
        'form': form,
    }
    return render(request, 'blog/upload_pdf.html', context)



def pdf_list(request):

    user_dept = request.user.profile.department
    user_level = request.user.profile.level
    pdf_list = Pdf_File.objects.filter(department=user_dept, level=user_level).exclude(books=request.user.id)
    post_pdf_list = MorePdfs.objects.filter(department=user_dept, level=user_level)

    
    context = {
        'pdf_list': pdf_list,
        'post_pdf_list': post_pdf_list,
    }

    return render(request, 'blog/pdf_list.html', context)


@login_required
def my_books(request):
    books = Pdf_File.objects.filter(books=request.user.pk)
    context = {
        'books': books,
    }
    return render(request, 'blog/my_books.html', context)

@login_required
def add_to_my_books(request, pk):
    pdf = get_object_or_404(Pdf_File, pk=pk)

    if pdf.books.filter(id=request.user.id).exists():
        messages.info(request, f'"{pdf.title}" already exist in your books')
    else:
        pdf.books.add(request.user)
        messages.info(request, f'Added "{pdf.title}" to your books')

    return redirect('pdf_list')


@login_required
def remove_from_my_books(request, pk):
    pdf = get_object_or_404(Pdf_File, pk=pk)

    if pdf.books.filter(id=request.user.id).exists():
        pdf.books.remove(request.user)
        messages.info(request, f'"{pdf.title}" have been removed from your books')
    else:
        messages.info(request, f'You don\'t have "{pdf.title}" in your books')

    return redirect('my_books')


