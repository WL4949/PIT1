from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
<<<<<<< HEAD
    return render(request, 'home.html', {'name':'Jean Paul.'})

=======
    return render(request, 'home.html', {'name':'Jean P'})
    
>>>>>>> 5d2002c4246db82bc383bb0897ff2416b63fc9bd
