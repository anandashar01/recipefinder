import csv
import re
from django.db import models
from django.forms import JSONField
class Recipe(models.Model):
    def __str__(self):
        return self.recipe_name
    recipe_name = models.CharField(max_length=200)
    ingredients = models.JSONField()
    recipe_URL = models.CharField(max_length=400)

    def update_recipes():
        with open('../webscraped_data/Recipes_1000.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                name = row[0]
                p = re.findall(r"'(.*?)'",row[1])
                ingr = {ing: 47 for ing in p}
                url = row[2]
                Recipe.objects.create(recipe_name=name, ingredients=ingr, recipe_URL=url)



class Fridge(models.Model):
    def __str__(self):
        return self.fridge_name

    staged_ingr = models.CharField(max_length=200)
    staged_amt = models.IntegerField()
    ingredients = models.JSONField() #ingredients[key]=value to set, pop to get

   
    fridge_name = models.CharField(max_length=200)
   
    def get_available_recipes(self):
        rv = []
        for r in Recipe.objects.all():
            if len(set(r.ingredients.keys())) == len(set((r.ingredients.keys())).intersection(set(self.ingredients.keys()))):
                rv.append(r.recipe_URL)

        return rv
        