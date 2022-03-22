from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm, BusinessForm, PostForm,NeighborhoodForm
from .models import Profile, Business, Post,Neighborhood
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    current_user = request.user
    businesses = Business.get_business()
    posts = Post.get_posts()

    return render(request, 'index.html', {'current_user': current_user, 'businesses': businesses, 'posts': posts})


def signup(request):
    name = 'Signup'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name': name})


@login_required(login_url='/login/')
def profile(request):
    current_user = request.user

    return render(request, 'profile.html', {'current_user': current_user, })

@login_required(login_url='/login/')
def update_profile(request):
    current_user = request.user
    profile = Profile(user=request.user)
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,  instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user, 'form':form})

@login_required(login_url='/login/')
def new_business(request):
    current_user = request.user

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user= current_user
            business.save()
        return redirect('home')
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'current_user':current_user, 'form':form})


@login_required(login_url='/login/')
def new_neighborhood(request):
    current_user = request.user

    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user= current_user
            neighborhood.save()
        return redirect('home')
    else:
        form = NeighborhoodForm()
    return render(request, 'newneighborhood.html', {'current_user':current_user, 'form':form})    

@login_required(login_url='/login/')
def all_neighborhood(request):
    all_neighborhood = Neighborhood.objects.all()
    all_neighborhood = all_neighborhood[::-1]
    params = {
        'all_neighborhood': all_neighborhood,
    }
    return render(request, 'all_neighborhood.html', params)

    
@login_required(login_url='/login/')
def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'current_user':current_user, 'form':form})