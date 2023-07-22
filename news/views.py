from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse ("welcome to my page")

blogs = [
    {'title': 'Ecobank in court',
     'content': 'Details',
     'date_posted': '2023-07-19',
     'reporter': 'AdaHarford',
    }
]

def blog_page(request):
    context = {
        'blogs' : blogs
    }
    return render (request,'news/blog.html', context)
