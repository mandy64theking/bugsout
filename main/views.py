from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    qs=Post.objects.filter(author=request.user)
    return render(request,'main/index.html',{'main_qs':qs})
def feed(request):
    qs=Post.objects.all().order_by('-date_posted')
    return render(request, 'feed/index.html',{'data':qs})
def newbug(request):
    if request.method=="POST":
        form=newPostForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
    return render(request, 'newbug/index.html')
def postie(request,id):
    qs=Post.objects.get(id=id)
    return render(request,'my-post/index.html',{'post_qs':qs})