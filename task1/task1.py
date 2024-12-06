import sys

# Получаем значения
n = int(sys.argv[1])
m = int(sys.argv[2])

# Формируем массив
array = [i for i in range(1, n + 1)]

# Переменная для хранения результата
result = []
current_index = 0

# Проходим m раз
for _ in range(m):
    result.append(array[current_index])
    current_index = (current_index + m) % n

print("Полученный путь: " + ''.join(map(str, result)))
