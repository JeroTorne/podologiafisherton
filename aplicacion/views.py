from django.shortcuts import render
from .models import *
from .forms import *






#-------////----------INDEX--------////------------------# 

def index(request):
    return render (request, "aplicacion/index.html")

#-------////----------FIN INDEX--------////------------------# 


def staff(request):
    return render (request, "aplicacion/staff.html")




#-------////----------TURNOS--------////------------------# 

def turnos(request):
    return render (request, "aplicacion/turnos.html")

#-------////----------FIN TURNOS--------////------------------# 

