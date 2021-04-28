from django.shortcuts import render

from apps.novels.models import Novel, Chapter

# Create your views here.
def home(request):
    return render(request, 'home.html')