import random

def create_text_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

def get_unique_words(file_path):
    unique_words = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            unique_words.update(words)
    return list(unique_words)

def print_random_words(words, n):

    random_words = random.sample(words, min(n, len(words)))
    for index, word in enumerate(random_words, start=1):
        print(f"{index}. {word}")

file_path = 'text_with_words.txt'

text = "світ текст Земля слово демонстрація приклад повторювати система випадковий кодування"

create_text_file(file_path, text)
unique_words = get_unique_words(file_path)

n = int(input("Введіть кількість випадкових слів для виведення: "))

print("Випадкові слова:")
print_random_words(unique_words, n)
