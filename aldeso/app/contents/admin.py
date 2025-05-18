# contents/admin.py
from django.contrib import admin
from .models import HomePage, Contact, FooterLink

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "link", "order")
    list_editable = ("order",)

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")