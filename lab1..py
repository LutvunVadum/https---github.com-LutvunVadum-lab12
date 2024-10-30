def multiplication_table(n):
    """Виводить таблицю множення для чисел від 1 до N"""
    print("Таблиця множення:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

def pythagorean_table(n):
    """Виводить таблицю Піфагора для чисел від 1 до N"""
    print("\nТаблиця Піфагора:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

try:
    N = int(input("Введіть число N для таблиці множення та Піфагора: "))
    multiplication_table(N)
    pythagorean_table(N)
except ValueError:
    print("Помилка! Введіть коректне ціле число.")