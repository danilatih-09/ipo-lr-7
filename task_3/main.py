# Тихонович Данила Вариант 5
import json
import os

FILENAME = "cities.json"

def load_cities(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"Содержимое файла '{filename}':\n{content[:300]}...")
                return json.loads(content)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при загрузке данных: {e}")
    else:
        print(f" Файл '{filename}' не найден!")
    return []

def save_cities(cities, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(cities, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Ошибка при сохранении данных: {e}")
        return False

def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Ошибка: значение должно быть положительным.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите целое число.")

def read_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: поле не может быть пустым.")

def display_city(city, position=None):
    is_big_str = "большой (>100 000)" if city["is_big"] else "маленький (≤100 000)"
    if position is not None:
        print(f"Позиция в списке: {position}")
    print(f"ID: {city['id']}")
    print(f"Название: {city['name']}")
    print(f"Страна: {city['country']}")
    print(f"Статус: {is_big_str}")
    print(f"Население: {city['people_count']}")

def find_city_by_id(cities, target_id):
    for index, city in enumerate(cities):
        if city["id"] == target_id:
            return city, index + 1
    return None, None

def add_city(cities, name, country, people_count):
    new_id = max((c["id"] for c in cities), default=0) + 1
    is_big = people_count > 100000
    new_city = {
        "id": new_id,
        "name": name,
        "country": country,
        "is_big": is_big,
        "people_count": people_count
    }
    return cities + [new_city]

def remove_city_by_id(cities, target_id):
    new_cities = [c for c in cities if c["id"] != target_id]
    removed = len(new_cities) != len(cities)
    return new_cities, removed

def main():
    print("start code ...")
    cities = load_cities(FILENAME)
    print(f" Загружено {len(cities)} городов из '{FILENAME}'")
    operation_count = 0

    while True:
        print("\nМеню:")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю id")
        print("3. Добавить запись")
        print("4. Удалить запись по полю id")
        print("5. Выйти из программы")

        choice = input("Выберите пункт меню (1–5): ").strip()

        if choice == "1":
            print("\n============== Все записи ==============")
            if not cities:
                print("Нет записей.")
            else:
                for city in cities:
                    print("-" * 40)
                    display_city(city)
            operation_count += 1

        elif choice == "2":
            target_id = read_positive_int("Введите ID города: ")
            city, pos = find_city_by_id(cities, target_id)
            if city is not None:
                print("\n============== Найдено ==============")
                display_city(city, pos)
            else:
                print("\n============== Не найдено ===============")
            operation_count += 1

        elif choice == "3":
            name = read_non_empty_string("Введите название города: ")
            country = read_non_empty_string("Введите страну: ")
            people_count = read_positive_int("Введите численность населения: ")
            cities = add_city(cities, name, country, people_count)
            if save_cities(cities, FILENAME):
                print("Запись успешно добавлена.")
            operation_count += 1

        elif choice == "4":
            target_id = read_positive_int("Введите ID города для удаления: ")
            cities, removed = remove_city_by_id(cities, target_id)
            if removed:
                if save_cities(cities, FILENAME):
                    print("Запись успешно удалена.")
            else:
                print("\n============== Не найдено ===============")
            operation_count += 1

        elif choice == "5":
            print(f"\nВыполнено операций: {operation_count}")
            print("... end code")
            break

        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")

if __name__ == "__main__":
    main()