# dirty_main.py
from приложение.salary import *
from приложение.база_данных.people import *
from datetime import datetime


def dirty_main():
    """
    Альтернативная версия main.py с импортом всех функций через *
    """
    print("Запуск через dirty_main.py")
    current_date = datetime.now().date()
    print(f"Текущая дата: {current_date}")
    print("-" * 40)

    # Теперь функции доступны напрямую, без указания модулей
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    dirty_main()