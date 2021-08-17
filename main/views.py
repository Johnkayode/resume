from django.shortcuts import render, redirect

from .models import Contact


def home(request):
    return render(request, 'index.html')

def contact(request):

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST["email"]
        subject = request.POST["subject"]
        note = request.POST["message"]

        contact = Contact.objects.create(
            email=email,
            subject = subject,
            note =  note
        )
        contact.save()

    return redirect('home')

