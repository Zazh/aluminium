# contents/views.py
from django.shortcuts import render
from .models import HomePage, Contact, FooterLink

def home_view(request):
    homepage = HomePage.objects.first()  # предполагаем, что одна запись
    contacts = Contact.objects.all()
    footer_links = FooterLink.objects.all()

    context = {
        "homepage": homepage,
        "contacts": contacts,
        "footer_links": footer_links,
    }
    return render(request, "home.html", context)