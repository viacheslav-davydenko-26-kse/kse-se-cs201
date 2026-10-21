# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

print("# ---------- Завдання 4.1 (просте) — math і datetime ----------")
# Напишіть дві функції:
#
# а) circle_stats(radius) — повертає словник
#       {"area": ..., "circumference": ...}
#    де площа й довжина кола обчислені через math.pi і округлені до 2 знаків.
#
# б) days_until(deadline, today) — обидва аргументи — рядки у форматі
#    "дд.мм.рррр". Повертає ціле число днів від today до deadline
#    (від'ємне, якщо дедлайн уже минув; 0, якщо це той самий день).
#    Використайте datetime.strptime("%d.%m.%Y") та різницю дат (.days).
#
# Функції не мають нічого друкувати.
import math
from datetime import datetime


def circle_stats(radius):
    stats = {} 
    stats["area"] = round(math.pi * radius ** 2, 2)
    stats["circumference"] = round(2 * math.pi * radius, 2)
    return stats


def days_until(deadline, today):
    deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
    today_date = datetime.strptime(today, "%d.%m.%Y")
    delta_date = deadline_date - today_date
    return delta_date.days 

print(circle_stats(5))                           # очікується: {'area': 78.54, 'circumference': 31.42}
print(circle_stats(1))                           # очікується: {'area': 3.14, 'circumference': 6.28}
print(days_until("20.12.2024", "01.12.2024"))    # очікується: 19
print(days_until("01.12.2024", "20.12.2024"))    # очікується: -19
print(days_until("15.03.2024", "15.03.2024"))    # очікується: 0


print("# %% ---------- Завдання 4.2 (середнє) — власний модуль ----------")
# а) Створіть поруч файл text_tools.py з двома функціями:
#      word_count(text)   — кількість слів у рядку (слова розділені пробілами;
#                           з обох кінців кожного слова приберіть ".,!?;:",
#                           порожні слова після очищення не враховуйте);
#      longest_word(text) — найдовше слово (після очищення від розділових
#                           знаків, регістр не змінюйте); якщо таких кілька —
#                           перше за порядком; для порожнього тексту — "".
#    Наприкінці файлу додайте блок if __name__ == "__main__": який друкує
#    "text_tools self-test" і викликає обидві функції на будь-якому прикладі.
# б) Тут імпортуйте модуль (import text_tools as tt) і виведіть результати.
#    Переконайтесь, що під час імпорту "text_tools self-test" НЕ друкується.
#
# Очікується:
#   print(tt.word_count("Hello, world! Hello Python."))   # 4
#   print(tt.word_count("...!!!"))                        # 0
#   print(tt.word_count(""))                              # 0
#   print(tt.longest_word("a bb ccc dd"))                 # ccc
#   print(tt.longest_word("Hi, There!"))                  # There
#   print(repr(tt.longest_word("")))                      # ''
# Ваш код тут (імпорт і виклики):
import text_tools as tt

print(tt.word_count("Hello, world! Hello Python."))   # 4
print(tt.word_count("...!!!"))                        # 0
print(tt.word_count(""))                              # 0
print(tt.longest_word("a bb ccc dd"))                 # ccc
print(tt.longest_word("Hi, There!"))                  # There
print(repr(tt.longest_word("")))                      # ''

print("# %% ---------- Завдання 4.3 (потрібен інтернет) — requests ----------")
# Напишіть функцію get_todo_title(todo_id), яка робить GET-запит на
#   https://jsonplaceholder.typicode.com/todos/<todo_id>
# (з timeout=10), перевіряє успіх через response.raise_for_status() і
# повертає поле "title". Якщо сталась помилка requests
# (requests.exceptions.RequestException, зокрема 404) — поверніть None.
#
# Очікується:
#   print(get_todo_title(1))        # delectus aut autem
#   print(get_todo_title(99999))    # None
import requests


def get_todo_title(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["title"]
    except requests.exceptions.RequestException:
        return None

print(get_todo_title(1))
print(get_todo_title(99999))
