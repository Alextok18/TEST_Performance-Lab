import json
import sys
import os

def update_test_values(tests_object, values_dict):
    test_id = tests_object.get("id")
    if test_id is not None and test_id in values_dict:
        tests_object["value"] = values_dict[test_id]

    for key in ["values", "tests"]:
        nested_objects = tests_object.get(key)
        if nested_objects:
            for nested_object in nested_objects:
                update_test_values(nested_object, values_dict)

def load_values_dict(values_object):
    return {item["id"]: item["value"] for item in values_object.get("values", [])}

def main():
    # Проверяем количество аргументов
    if len(sys.argv) != 4:
        print("Ошибка: требуется три пути к файлам (tests.json, values.json, report.json).")
        sys.exit(1)

    tests_json_path = sys.argv[1]
    values_json_path = sys.argv[2]
    report_json_path = sys.argv[3]

    try:
        with open(tests_json_path, "r", encoding="utf-8") as tests_file:
            tests_object = json.load(tests_file)

        with open(values_json_path, "r", encoding="utf-8") as values_file:
            values_object = json.load(values_file)

        values_dict = load_values_dict(values_object)

        update_test_values(tests_object, values_dict)

        with open(report_json_path, "w", encoding="utf-8") as report_file:
            json.dump(tests_object, report_file, ensure_ascii=False, indent=4)

        print(f"Результат успешно сохранен в '{report_json_path}'.")

    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e.filename}")
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
