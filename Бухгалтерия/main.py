# main.py
from приложение.salary import calculate_salary
from приложение.база_данных.people import get_employees
from datetime import datetime


def main():
    """
    Основная функция программы, вызывает расчет зарплаты и получение сотрудников
    с выводом текущей даты
    """
    # Вывод текущей даты
    current_date = datetime.now().date()
    print(f"Текущая дата: {current_date}")
    print("-" * 40)

    # Вызов функции расчета зарплаты
    calculate_salary()

    # Вызов функции получения сотрудников
    get_employees()


if __name__ == '__main__':
    main()