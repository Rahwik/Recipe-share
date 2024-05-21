from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
             data = request.POST

             recipe_name = data.get('recipe_name')
             recipe_description = data.get('recipe_description')
             recipe_image = request.FILES.get('recipe_image')
            

             Recipe.objects.create(
                recipe_name = recipe_name,
                recipe_description = recipe_description,
                recipe_image = recipe_image,

            )
             return redirect('/recipes/')

    return render(request,'recipes.html')

@login_required(login_url="/login/")
def shared(request):
    context={'page':'about'}
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains =  request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, "shared.html",context)

@login_required(login_url="/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method =="POST":
         data = request.POST

         recipe_name = data.get('recipe_name')
         recipe_description = data.get('recipe_description')
         recipe_image = request.FILES.get('recipe_image')

         queryset.recipe_name = recipe_name
         queryset.recipe_description = recipe_description

         if recipe_image:
            queryset.recipe_image = recipe_image
         queryset.save()  
         return redirect('/shared/')      




    context = {'recipe': queryset}
    return render(request, "update_recipe.html",context)   


@login_required(login_url="/login/")
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/shared/')

def login_page(request):
    if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('password')

         if not User.objects.filter(username = username).exists():
            messages.info(request, "UserName does not exists")
            return redirect("/login/")
         user = authenticate(username = username , password = password)

         if user is None:
            messages.info(request, "Inalid password")
            return redirect("/login/")
         else:
            login(request , user)
            return redirect("/recipes/")
            
       
    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')    

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already Taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created succesfully")
        
        return redirect("/login/")

    return render(request, 'register.html')
    
    



     

