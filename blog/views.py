from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Post
# Create your views here.

def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
