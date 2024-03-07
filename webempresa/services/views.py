from django.shortcuts import render
from .models import Service

# Create your views here.

#Este codigo es para devolver la pagina con datos estaticos
##def services(request):
    # Esta es la url que se mostrara : "services/services.html"
  ##  return render(request, "services/services.html")

#Esto muestra data dinamica
def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html", {'services':services})