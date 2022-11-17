
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ImageForm

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'myapp/result.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'myapp/out.html', {'form': form})

def home(request):
    count = User.objects.count()
    return render(request, "myapp/home.html", {"count": count})

def out(request):
    count = User.objects.count()
    return render(request, "myapp/out.html", {"count": count})    



# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("out")
#     else:
#         form = UserCreationForm()
#     return render(request, "registration/signup.html", {"form": form})

@login_required
def secret_page(request):
    return render(request, "myapp/secret_page.html")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "myapp/secret_page.html"


from myapp.models import User
from myapp.forms import CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("out")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

class SignUp(CreateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("result")
        return super().dispatch(request, *args, **kwargs)

    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("out")    
