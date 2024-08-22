import json
import sys

''' python task3.py values.json tests.json report.json '''


def update_test_values(tests, values_dict):
    for test in tests:
        # Обновляем значение поля "value", если id есть в values_dict
        if test["id"] in values_dict:
            test["value"] = values_dict[test["id"]]

        # Рекурсивно обрабатываем вложенные тесты
        if "values" in test:
            update_test_values(test["values"], values_dict)


def main(values_path, tests_path, report_path):
    # Чтение файла values.json
    with open(values_path, 'r') as f:
        values_data = json.load(f)

    # Преобразование списка values в словарь для удобства поиска по id
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Чтение файла tests.json
    with open(tests_path, 'r') as f:
        tests_data = json.load(f)

    # Обновление тестов на основе values_dict
    update_test_values(tests_data["tests"], values_dict)

    # Запись результата в report.json
    with open(report_path, 'w') as f:
        json.dump(tests_data, f, indent=4)


if __name__ == "__main__":
    # Получаем пути к файлам из аргументов командной строки
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)
