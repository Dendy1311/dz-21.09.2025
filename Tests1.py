documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def find_name_by_document_number():
    number = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == number:
            return doc['name']
    return 'Документ не найден'


def find_shelf_by_document_number():
    number = input('Введите номер документа: ')
    for shelf, docs in directories.items():
        if number in docs:
            return shelf
    return 'Документ не найден'


def list_all_documents():
    doc_list = []
    for doc in documents:
        doc_list.append(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    return '\n'.join(doc_list)


def add_document():
    number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    name = input('Введите имя владельца: ')
    shelf = input('Введите номер полки: ')

    if shelf not in directories:
        return 'Такой полки не существует'

    documents.append({"type": doc_type, "number": number, "name": name})
    directories[shelf].append(number)
    return 'Документ добавлен'


# Дополнительные команды (Задача №2)
def delete_document():
    number = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == number:
            documents.remove(doc)
            break
    else:
        return 'Документ не найден'

    for shelf in directories.values():
        if number in shelf:
            shelf.remove(number)
            return 'Документ удален'
    return 'Документ не найден в перечне полок'


def move_document():
    number = input('Введите номер документа: ')
    new_shelf = input('Введите целевую полку: ')

    if new_shelf not in directories:
        return 'Целевая полка не существует'

    current_shelf = None
    for shelf, docs in directories.items():
        if number in docs:
            current_shelf = shelf
            break

    if not current_shelf:
        return 'Документ не найден'

    directories[current_shelf].remove(number)
    directories[new_shelf].append(number)
    return 'Документ перемещен'


def add_shelf():
    shelf = input('Введите номер новой полки: ')
    if shelf in directories:
        return 'Такая полка уже существует'

    directories[shelf] = []
    return 'Полка добавлена'


def main():
    commands = {
        'p': find_name_by_document_number,
        's': find_shelf_by_document_number,
        'l': list_all_documents,
        'a': add_document,
        'd': delete_document,
        'm': move_document,
        'as': add_shelf
    }

    while True:
        command = input('\nВведите команду (p/s/l/a/d/m/as/q для выхода): ').strip()
        if command == 'q':
            break
        if command in commands:
            result = commands[command]()
            print(result)
        else:
            print('Неверная команда')


if __name__ == '__main__':
    main()