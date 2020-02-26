from django.shortcuts import render
from .utils import get_ionicons

def demo(request):
    return render(request, "django_static_ionicons/demo.html", {
        "ionicons": get_ionicons(),
    })
