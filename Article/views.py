from django.shortcuts import render
from django.http import HttpResponse
from Article.models import Articles
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    posts = Articles.objects.all()
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':post_list})

def detail(request, id):
    try:
        post = Articles.objects.get(id=str(id))
    except Articles.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def archives(request):
    try:
        post_list=Articles.objects.all()
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'archives.html',{'post_list': post_list,'error':False})

def search_tag(request, tag):
    if tag==None:
        return render(request,'tag.html',{"error":True})
    else :
        try:
            post_list = Articles.objects.filter(category__iexact = tag)
        except Articles.DoesNotExist:
            raise Http404
        return render(request, 'tag.html', {'post_list':post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Articles.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request,'archives.html',{'post_list':post_list,'error':True})
            else :
                return render(request,'archives.html',{'post_list':post_list,'error':False})
    return redirect('/')
