from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm


def register_view(request):
    """
    Handle new user registration.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # email is already present via form
            user.email = form.cleaned_data.get("email")
            user.save()
            # Log the user in immediately after registration (optional)
            login(request, user)
            return redirect("blog:profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    """
    Show and edit user profile.
    """
    profile = request.user.profile
    if request.method == "POST":
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if pform.is_valid():
            pform.save()
            return redirect("blog:profile")
    else:
        pform = ProfileForm(instance=profile)

    return render(request, "blog/profile.html", {"pform": pform})
