from django.shortcuts import render

def calculator(request):
    return render(request, 'index.html')  # Make sure this points to 'index.html'
