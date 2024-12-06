import sys
import math

if len(sys.argv) < 3:
    print("Ошибка: Укажите пути к двум файлам.")
    sys.exit(1)

ctrName = sys.argv[1]
pntName = sys.argv[2]

try:
    # Чтение  центра окружности и радиуса
    with open(ctrName) as centerFile:
        centerX, centerY = map(float, centerFile.readline().split())
        rad = float(centerFile.readline().strip())

    # Чтение файла с точками
    with open(pntName) as pointFile:
        result = []

        for line in pointFile:
            try:
                pointX, pointY = map(float, line.strip().split())
                # Вычисление расстояния от точки до центра окружности
                dist = math.sqrt((pointX - centerX) ** 2 + (pointY - centerY) ** 2)

                # Определение положения точки
                if dist < rad:
                    result.append("1")  # Точка внутри
                elif dist == rad:
                    result.append("0")  # Точка на окружности
                else:
                    result.append("2")  # Точка снаружи
            except ValueError:
                print(f"Ошибка: строка '{line.strip()}' имеет некорректный формат.")
                continue

    print("\n".join(result))

except FileNotFoundError as e:
    print("Файл не найден:", e.filename)
except ValueError as e:
    print("Ошибка в данных файла:", e)
