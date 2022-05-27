from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
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
    if request.method=="POST":
        form=newCommentForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data["text"]
            instance=form.save(commit=False)
            instance.author=request.user
            instance.post_connected=qs
            instance.save()
    cc=Comment.objects.filter(post_connected=qs)
    return render(request,'my-post/index.html',{'post_qs':qs,'comment_ps':cc})
def feedback(request):
    if request.method=="POST":
        form=feedbackForm(request.POST)
        if form.is_valid():
            rating=form.cleaned_data["rating"]
            commentid=form.cleaned_data["commentid"]
            instance=form.save(commit=False)
            instance.comment_connected=Comment.objects.get(id=commentid)
            instance.user_connected=Comment.objects.get(id=commentid).author
            instance.save()
    return(redirect('/feed'))
def leaderboard(request):
    userall=User.objects.all()
    dict={}
    i=0
    cols=3
    rows=10
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for k in userall:
        fk=Feedback.objects.filter(user_connected=k).count()
        tk=Feedback.objects.filter(user_connected=k)
        sum=0
        try :
            sum=sum+tk[0].rating
        except :
            sum=sum+0
        arr[i][0]=k
        arr[i][1]=fk
        if  fk!=0:
            arr[i][2]=sum/fk
        else:
            arr[i][2]=0
        i=i+1
    arr.sort(key=lambda x:x[1] ,reverse=True)
    print(arr)
    return(render(request,'leaderboard/index.html',{'users':arr}))