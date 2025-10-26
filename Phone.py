import csv
import re
from pprint import pprint


def parse_fio(contact):
    """Функция для разделения ФИО на отдельные компоненты"""
    # Объединяем первые три поля и разбиваем по пробелам
    fio = ' '.join(contact[:3]).split()


    lastname = fio[0] if len(fio) > 0 else ''
    firstname = fio[1] if len(fio) > 1 else ''
    surname = fio[2] if len(fio) > 2 else ''

    return lastname, firstname, surname


def format_phone(phone):
    """Функция для приведения телефонов к стандартному формату"""
    if not phone:
        return ''


    cleaned_phone = re.sub(r'[^\d+]', '', phone)


    if cleaned_phone.startswith('8'):
        cleaned_phone = '7' + cleaned_phone[1:]


    match = re.search(r'7(\d{10})$', cleaned_phone)
    if match:
        formatted = f"+7({match.group(1)[:3]}){match.group(1)[3:6]}-{match.group(1)[6:8]}-{match.group(1)[8:10]}"
    else:
        # Если не удалось извлечь 10 цифр, возвращаем исходный номер
        return phone


    ext_match = re.search(r'доб\.?\s*(\d+)', phone, re.IGNORECASE)
    if ext_match:
        formatted += f" доб.{ext_match.group(1)}"

    return formatted


def merge_contacts(contacts_list):
    """Функция для объединения дублирующихся записей"""
    merged = {}

    for contact in contacts_list:
        key = (contact[0], contact[1])

        if key not in merged:
            merged[key] = contact
        else:
            existing = merged[key]
            for i in range(len(contact)):
                if existing[i] == '' and contact[i] != '':
                    existing[i] = contact[i]

    return list(merged.values())


# Считываем адресную книгу
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

print("Исходные данные:")
pprint(contacts_list)

header = contacts_list[0]
processed_contacts = []


for contact in contacts_list[1:]:
    # Приводим ФИО к правильному формату
    lastname, firstname, surname = parse_fio(contact)


    new_contact = [
        lastname,
        firstname,
        surname,
        contact[3],
        contact[4],
    ]

    processed_contacts.append(new_contact)


merged_contacts = merge_contacts(processed_contacts)


final_contacts = [header] + merged_contacts

print("\nОбработанные данные:")
pprint(final_contacts)


with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts)

print("\nДанные сохранены в файл 'phonebook.csv'")