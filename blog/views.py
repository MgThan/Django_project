from django.shortcuts import render

posts = [{
        'author':'Maung Maung',
        'title':'First Blog Post',
        'content':'first post',
        'date_posted':'May 6,2020'
    },
    {
        'author': 'Aaung Aaung',
        'title': 'Secont Blog Post',
        'content': 'second post',
        'date_posted': 'May 6,2020'
    }]
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
def homePage(request):
    return render(request,'blog/base.html')

# Create your views here.
