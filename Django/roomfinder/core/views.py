from django.shortcuts import render

from .models import Room


# Create your views here.
def list_it(request):

    rooms = Room.objects.all()

    return render(request, "list.html" , {
        "all_rooms" : rooms,
        "num":4.12131313123132
    })


def home(req):
    return render(req, "home.html")



def about(req):
    return render(req, "about.html")