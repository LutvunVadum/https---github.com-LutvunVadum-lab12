import digit_operations as do

def main():
    number = int(input("Введіть натуральне число: "))

    even_count = do.count_even_digits(number)
    print(f"Кількість парних цифр у числі {number}: {even_count}")

    odd_product = do.product_of_odd_digits(number)
    print(f"Добуток непарних цифр у числі {number}: {odd_product}")

if __name__ == "__main__":
    main()