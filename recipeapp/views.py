from django.shortcuts import render,redirect
from .models import *

# Create your views here.


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

def shared(request):
    context={'page':'about'}
    queryset = Recipe.objects.all()
    context = {'recipes': queryset}
    return render(request, "shared.html",context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/shared/')
    



     

