n = int(input("Введите высоту треугольника: "))

row = [1]  # Первая строка

for _ in range(n):
    print(*row)
    
    # Создаём следующую строку
    row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]