from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# @login_required
# def profile(request):
#     user = get_object_or_404(User, username=request.user)
#     posts = Post.objects.all().filter(author=request.user).order_by('-date_posted')

#     paginator = Paginator(posts, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.page(page_number)

#     context = {
#         'posts': posts,
#         'page_obj': page_obj
#     }

    # return render(request, 'profile.html', context)

class UserProfileView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # request.POST to take in the new data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # request.FILES for the image
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated')
            return redirect('blog-home')
    else:
        u_form = UserUpdateForm(instance=request.user) # to populate the form field with existing data
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile_update.html', context)