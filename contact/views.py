from django.shortcuts import render, HttpResponse, redirect
from contact.models import Contact


# Create your views here.
def index(request):
    context = {"variable": " i am from context"}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html ")


def show_contacts(request):
    saved_contacts = Contact.objects.all()
    return render(request, "show_contacts.html", {"contacts": saved_contacts})


def contact(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        # debug Print
        print(username, email, phone, password)

        # Check if email already exists
        if Contact.objects.filter(email=email).exists():
            return render(
                request,
                "contact.html",
                {"email_error": "This email is already registered."},
            )

        # Check if phone already exists
        if Contact.objects.filter(phone=phone).exists():
            return render(
                request,
                "contact.html",
                {"num_error": "This phone number is already registered."},
            )

        Contact.objects.create(
            username=username, email=email, phone=phone, password=password
        )

        return render(
            request,
            "contact.html",
            {"success_message": "Your form has been submitted successfully."},
        )

    # If GET request
    return render(request, "contact.html")


def view_contact(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, "contact_view.html", {"contact": contact})


def edit_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == "POST":
        contact.username = request.POST.get("username")
        contact.email = request.POST.get("email")
        contact.phone = request.POST.get("phone")
        contact.save()
        return redirect("show_contacts")

    return render(request, "contact_edit.html", {"contact": contact})


def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect("show_contacts")
