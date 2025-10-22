def read_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ing_line = file.readline().strip()
                name, quantity, measure = map(str.strip, ing_line.split('|'))
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Пропуск пустой строки
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def merge_files(file_list, output_file):
    files_data = []
    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            files_data.append({
                'name': filename,
                'line_count': len(lines),
                'content': lines
            })

    files_data.sort(key=lambda x: x['line_count'])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_info in files_data:
            out_file.write(f"{file_info['name']}\n")
            out_file.write(f"{file_info['line_count']}\n")
            out_file.writelines(file_info['content'])
            out_file.write('\n')


#Пример
if name == '__main__':
    # Задача 1
    cook_book = read_cook_book('recipes.txt')
    print("CookBook:", cook_book)

    #Задача 2
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
    print("Shopping List:", shop_list)

    #Задача 3
    merge_files(['1.txt', '2.txt', '3.txt'], 'result.txt')