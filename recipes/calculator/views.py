from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def get_recipe(request):
    servings = request.GET.get('servings', 1)
    recipe_name = request.path
    recipe_name = ''. join(simb for simb in recipe_name if simb.isalpha())
    for recipe, ingredients in DATA.items():
        if servings != 1:
            new_dict_ingredients = {}
            for ingredient, count in ingredients.items():
                new_dict_ingredients[ingredient] = count * int(servings)
        else:
            new_dict_ingredients = ingredients
        if recipe == recipe_name:
            context = {
                'recipe': new_dict_ingredients
            }
            break
    return render(request, 'calculator/index.html', context)