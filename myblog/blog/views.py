from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication




class CreateUserView(generics.CreateAPIView):
    
    # here we are specifying the different objs that we're going to be looking for  at when we're creating a new one to make sure 
    # we don't create a user that already exist.Then serializer class which tells this view what kind of data we need to accept to make a new user.
    # Then permisssion class specify who can actually call  this in this case we're going to allow anyone even if they are not authenticated to use this view to create a new user
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
# Create your views here.
def home(request):

    output = _("")
    print(f"Output in {get_language()}: {output}")


    # load all the post from db(10)
    posts= Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts':posts,
        'cats':cats,
        'output':output
    }
    return render(request, 'home.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post':post, 'cats':cats})


def category(request,urls):

    cat= Category.objects.get(urls = urls)
    posts = Post.objects.filter(cat = cat)
    return render(request,"category.html",{'cat':cat, 'posts':posts})
