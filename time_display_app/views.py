from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    context = {
        "name" : "Lauren",
        "time" : datetime.datetime.now(),
    }
    return render(request, 'index.html', context)