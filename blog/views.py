from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from blog.forms import RegisterForm,loginForm,createBlogForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from blog.models import Post
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('pub_date')
    return render_to_response('index.html', {'posts': posts,  "request":request})

def post(request,id):
    try:
        post = Post.objects.get(id=id)
        author =post.author
    except Post.DoesNotExist:
        raise Http404
    return render_to_response("post.html", {"post": post, "author": author,"request":request})

@login_required(login_url="/login/")
def personal(request,id):
    try:
        user = User.objects.get(id=id)
        posts = user.post_set.all()
    except User.DoesNotExist:
        raise Http404
    return render_to_response("personal.html", {"posts": posts, "user": user, "request":request})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if password == '' or username == '':
            state = 'there is empty.Please try again'
            return render_to_response('error.html', {'state': state})
        try:
            loginuser = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('personal', args=(loginuser.id,)))
            else:
                return HttpResponseRedirect(reverse('personal', args=(loginuser.id,)))
        else:
            state = 'not exist or password error'
            return render_to_response('error.html', {'state': state})
    else:
        form = loginForm()
        return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

@login_required(login_url="/login/")
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        if password == '' or password2 == ''or username == ''or email == '':
            state = 'there is empty.Please register again'
            return render_to_response('error.html', {'state': state})
        if password != password2:
            state = 'password is not same.Please register again'
            return render_to_response('error.html', {'state': state})
        elif User.objects.filter(username=username):
            state = 'username is exist.Please register again'
            return render_to_response('error.html', {'state': state})
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponseRedirect(reverse('personal', args=(user.id,)))
    else:
        form = RegisterForm()
    return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

@login_required(login_url="/login/")
def editBlog(request,id):
    post = Post.objects.get(id=id)
    author = post.author
    if request.method == 'POST':
        title = request.POST['title']
        Post_text = request.POST['Post_text']
        if title and Post_text:
            post.author=author
            post.Post_text=Post_text
            post.title=title
            post.save()
            return HttpResponseRedirect(reverse('personal', args=(author.id,)))
        else:
            state = 'title and Post_text are needed.Please try again'
            return render_to_response('error.html', {'state': state, 'request':request})
    else:
        form = createBlogForm()
        return render_to_response('editBlog.html', {'form': form, 'id':id , 'post': post}, context_instance=RequestContext(request))

@login_required(login_url="/login/")
def deleteBlog(request,id):
    try:
        post = Post.objects.get(id=id)
    except Exception:
        raise Http404
    if post:
        post.delete()
        user = post.author
        return HttpResponseRedirect(reverse('personal', args=(user.id,)))

@login_required(login_url="/login/")
def createBlog(request,id):
    if request.method == 'POST':
        title = request.POST['title']
        Post_text = request.POST['Post_text']
        if title and Post_text:
            author = User.objects.get(id=id)
            post = Post(author=author, Post_text=Post_text, title=title)
            post.save()
            return HttpResponseRedirect(reverse('personal', args=(author.id,)))
        else:
            state = 'title and Post_text are needed.Please try again'
            return render_to_response('error.html', {'state': state, 'request':request})
    else:
        form = createBlogForm()
        return render_to_response('createBlog.html', {'form': form, "id":id}, context_instance=RequestContext(request))
















