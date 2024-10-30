def count_even_digits(number):
    even_count = 0
    while number > 0:
        digit = number % 10  
        if digit % 2 == 0:  
            even_count += 1
        number //= 10 
    return even_count

def product_of_odd_digits(number):
    product = 1
    has_odd = False
    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            product *= digit
            has_odd = True
        number //= 10
    return product if has_odd else 0
