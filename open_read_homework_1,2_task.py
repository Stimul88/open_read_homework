import os

with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = int(f.readline())
        dish_ingr = []
        for i in range(ingredient_count):
            emp = f.readline()
            ingredient_name, quantity, measure = emp.split(' | ')
            dish_ingr.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = dish_ingr

def get_shop_list_by_dishes(dishes, person_count):
    dict_ ={}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                dict_[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': int(ing['quantity']) * person_count}
    return dict_
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



