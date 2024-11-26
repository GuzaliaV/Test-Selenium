import random
import json

# Генерация случайного значения
name_BU_text = f"BU_тест_{random.randint(100, 999)}"

# Сохранение значения в config.json
config = {"name_BU_text": name_BU_text}
with open('config.json', 'w') as json_file:
    json.dump(config, json_file)

print(f"Сохранено значение: {name_BU_text}")
