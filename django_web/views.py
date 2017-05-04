from django.shortcuts import render


# Create your views here.

def index(request):
    context ={
        'p':'nihao'
    }
    return render(request, 'index.html',context)

