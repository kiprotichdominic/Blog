from django.shortcuts import render
from django.http import HttpResponse

posts= [
    {
        "author": "Kiprotich",
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
        {
        "author": "Kiprotich Dommie",
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2018'
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request,'blog/about.html',  {'title': 'About Page'})