# Домашнее задание по записи в файл и чтению из файла.
cook_book = {}
with open('recipes.txt', encoding = 'cp1251') as f:
    l0 = f.readlines()
    #print(l0)
    list1 = [l.strip() for l in l0]
    #print(list1)
    for el in list1:
        if el == '':
            k = list1.remove('')
    #print(list1)
    j = 0
    while j < len(list1):
        dish = list1[j]
        k = int(list1[j + 1])
        #print(k)
        cook_book[dish] = []
        for i in range(j + 2,j+2+k):
            d_in = {}
            sp_ingr = []
            sp_ingr = list1[i].split("|")
            d_in['ingredient_name'] = sp_ingr[0]
            d_in['quantity'] = sp_ingr[1]
            d_in['measure'] = sp_ingr[2]
            cook_book[dish].append(d_in)
        j += (2 + k)
    from pprint import pprint
    pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    dic_perchases={}
    for dish, ingredient in cook_book.items():
        if dish in dishes:
            for i in range(len(cook_book[dish])):
                key = ingredient[i]['ingredient_name']
                if key not in dic_perchases.keys():
                    dic_perchases[key] = {}
                    dic_perchases[key]['measure'] = ingredient[i]['measure']
                    dic_perchases[key]['quantity'] = int(ingredient[i]['quantity']) * person_count
                else:
                    dic_perchases[key]['quantity'] += int(ingredient[i]['quantity']) * person_count
    pprint(dic_perchases)
get_shop_list_by_dishes(["Омлет","Фахитос", "Запеченный картофель"], 2)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
