from django.shortcuts import render

# Create your views here.
def squanch(request):
    return render(request, 'index.html')
