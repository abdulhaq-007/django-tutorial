from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from .models import User
# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # add user to group
            # gp = Group.objects.get(name="users")
            # user.groups.add(gp.id)
            user.save()
            # login new user
            messages.add_message(request, messages.SUCCESS, "Well done !")
            return redirect("/")
        else:
            messages.add_message(request, messages.WARNING,
                                 "Something went wrong !")
    else:
        return render(request, "registration/register.html", {"form": form})
    return render(request, "registration/register.html", {"form": form})