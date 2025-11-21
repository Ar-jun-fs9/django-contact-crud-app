from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("show_contacts/", views.show_contacts, name="show_contacts"),
    path("contacts/<int:id>/", views.view_contact, name="view_contact"),
    path("contacts/<int:id>/edit/", views.edit_contact, name="edit_contact"),
    path("contacts/<int:id>/delete/", views.delete_contact, name="delete_contact"),
]
