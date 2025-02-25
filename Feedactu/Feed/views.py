from django.shortcuts import render
from Feed.models import Messages,Phrases

# Create your views here.


def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        Messages.objects.create(content=content, user=user)
        

    context = {}
    context['messages'] = Messages.objects.all()
    return render(request,'home.html',context=context)

def autre(request):
    if request.method == 'POST':
        ms = request.POST.get('ms')
        Phrases.objects.create(Ph=ms)
    context = {}
    context['Ms'] = Phrases.objects.all()

    return render(request, 'autre.html', context)