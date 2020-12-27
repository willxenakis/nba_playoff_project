from django.shortcuts import render

# Create your views here.

def predictions(request):
    return render(request, "predictions.html")
