from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    #instanciamos el formulario
    contact_form = ContactForm()
    if request.method == "POST":
        #llenamos el formulario 
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Suponiendo que todo esta ok
            #asunto,cuerpo,email_origen,email_destimo,reply_to
            email_enviar = EmailMessage(               
                subject="La Caffettiera: Nuevo mensaje de contacto",
                body="De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                from_email="no-contestar@inbox.mailtrap.io",
                to=["sistemas@cienpies.com.pe"],
                reply_to=[email]
            )
            try:
                email_enviar.send()
                return redirect(reverse('contact')+"?ok")  
            except Exception as e:
                #"algo no va bien"
                print(e)
                return redirect(reverse('contact')+"?fail")   
            return redirect(reverse('contact')+"?ok")
    return render(request, "contact/contact.html",{'form':contact_form})