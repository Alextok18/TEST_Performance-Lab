import sys


def read(fileName):
    """
    Читает числа из файла.
    """
    nums = []
    with open(fileName) as file:
        for line in file:
            nums.extend(map(int, line.split()))
    return nums


def findMin(nums):
    """
    Находит минимальное количество операций.
    """
    minVal = min(nums)  # Минимальное значение в массиве
    maxVal = max(nums)  # Максимальное значение в массиве

    # Полный перебор по всем возможным значениям
    minMoves = float('inf')  # Начальное значение для минимальных ходов
    for target in range(minVal, maxVal + 1):
        moves = sum(abs(num - target) for num in nums)  # Подсчитываем шаги для текущей цели
        if moves < minMoves:  # Обновляем минимальное количество шагов
            minMoves = moves

    return minMoves


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python script.py <имя_файла>")
        sys.exit(1)

    fileName = sys.argv[1]
    nums = read(fileName)
    minMoves = findMin(nums)
    print(minMoves)
