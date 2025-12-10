# Тихонович Данила Вариант 5 

import json

print("start code...")

with open ("task_2/dump.json", "r", encoding="utf-8") as file:
    data = json.load(file)

user_code = input(str("Введите номер квалиффикации: "))

found = False

for item in data:
    if item.get("model") == "data.specialty":
        fields = item.get("fields", {})
        code = fields.get("code")
        if code == user_code:
            specialty = fields.get("title", "не указано")
            qualification = fields.get("model", "не указано")
            level = fields.get("c_type", "не указано")

            print("================ Найдено =================")
            print(f'{code} >> Специальность "{specialty}", "{level}"')
            print(f'{code}-02 >> Квалификация "{qualification}"')
            found = True
            break

if not found:
    print("================ Не найдено =================")

print("end code")