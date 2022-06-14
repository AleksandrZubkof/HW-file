from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    units_of_measurement = ['ingredient_name', 'quantity', 'measure']
    for line in file:
        name_dish = line.strip()
        quantity = int(file.readline())
        ingredients_list = []
        for item in range(quantity):
            data = file.readline().strip().split('|')
            ingredients = {units_of_measurement[0]: data[0], units_of_measurement[1]: data[1],
                           units_of_measurement[2]: data[2]}
            ingredients_list.append(ingredients)
        cook_book[name_dish.strip()] = ingredients_list
        file.readline()
    pprint(cook_book)

print('----------------------')


def get_shop_list_by_dishes(dishes, person_count=1):
    result = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            pprint('Отсутствует блюдо')
            return
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in result.keys():
                key = ingredient['ingredient_name']
                value = {'measure': ingredient['measure'], 'quantity': (int(ingredient['quantity']) * person_count)}
                result[key] = value
            else:
                result[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count

    pprint(result)


get_shop_list_by_dishes(['Омлет'], 1)
