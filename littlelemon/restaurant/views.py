from django.shortcuts import render 

# View function to print Hello.
def index(request):
    return render(request, 'index.html', {})
