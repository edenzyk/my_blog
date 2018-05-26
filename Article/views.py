from django.shortcuts import render
from django.http import HttpResponse
from Article.models import Articles
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Articles.objects.all()
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
    except:
        raise Http404
    return render(request, 'archives.html',{'post_list': post_list,'error':False})
