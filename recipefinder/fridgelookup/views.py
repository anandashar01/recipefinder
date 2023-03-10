from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django import forms
from .forms import FridgeForm2
from .models import Fridge, Recipe

def index(request): #add fridge button, a list of fridges
    fridge_list = Fridge.objects.all() 
    template = loader.get_template('fridgelookup/index.html')
    context = {
        'fridge_list': fridge_list
    }
    return render(request, 'fridgelookup/index.html', context)

def results(request, fridge_id): #will show the results (available recipes' urls) for given fridge
    
    if request.method=="GET":

        fridge = get_object_or_404(Fridge, pk=fridge_id)
        recipe_list = fridge.get_available_recipes()

        context = {
        "fridge_name": fridge.fridge_name,
        'recipe_list': recipe_list
        }

        return render(request, 'fridgelookup/results.html', context)
    return

def detail(request, fridge_id):#shows fridge contents
    fridge = get_object_or_404(Fridge, pk=fridge_id)
    fridge = Fridge.objects.get(pk=1)
    fridge.save()
    form = FridgeForm2(instance=fridge)
    context = {
        'fridge': fridge,
        'ingredients': fridge.ingredients.keys(),
        'form': form
    }
    print("got to 38")
    form = FridgeForm2(instance=fridge)
    return render(request, 'fridgelookup/detail.html', context)

def update(request, fridge_id):
    fridge = get_object_or_404(Fridge, pk=fridge_id)

    if request.method == "POST":
        form = FridgeForm2(request.POST, instance=fridge)
        print("got to 37")
        if form.is_valid():
            print("got to 39")
            fridge = form.save()
            fridge.ingredients[fridge.staged_ingr] = fridge.staged_amt
            
            fridge.save()
            return HttpResponseRedirect(reverse('fridgelookup:detail', args=(fridge.id,)))
    

    return render(request, 'fridgelookup/detail.html', {'form': form, 'fridge': fridge})    
    