import json

# Загрузка значения из config.json
with open('config.json', 'r') as json_file:
    config = json.load(json_file)

name_BU_text = config['name_BU_text']
print(f"Загружено значение: {name_BU_text}")

# Использование переменной
def some_function():
    # Здесь вы можете использовать name_BU_text
    print(f"Используем значение: {name_BU_text}")

some_function()
