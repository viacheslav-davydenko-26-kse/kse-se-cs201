"""
Практична робота — Бібліотеки та модулі
Теми: math, random, datetime, власні модулі, pandas, matplotlib, requests

Структура (50 хв):
1. Питання                      — 10 хв
2. Розбір базових завдань        — 15 хв
3. Дебагінг                      — 10 хв
4. Самостійне написання коду     — 15 хв

Комірки розділені "# %%" — у VS Code / Jupyter їх можна запускати по одній.
Поруч із цим файлом мають лежати class_scores.csv і class_utils.py.
Потрібні бібліотеки: pip install pandas matplotlib requests
У блоці 3 помилки в коді очікувані, тому запускайте кожну комірку окремо.
Завдання 4.4 (бонус) потребує інтернету.
"""


# %% ========== БЛОК 1. ПИТАННЯ (10 хв) ==========
"""
Концептуальні питання до студентів:

1. Чим відрізняються модуль, пакет і бібліотека? Чому корисно не писати весь
   код в одному файлі, а підключати готові модулі?
2. Порівняйте три форми імпорту: import math, from math import sqrt та
   import pandas as pd. Коли доречна кожна з них і чому не рекомендують
   писати from math import *?
3. Чим вбудовані бібліотеки відрізняються від сторонніх? Навіщо потрібні pip,
   віртуальне середовище та файл requirements.txt?
4. Як Python шукає модуль, який ви імпортуєте? Що станеться, якщо назвати
   власний файл random.py і зробити import random?
5. Що робить блок if __name__ == "__main__": і яку проблему він розв'язує?
6. Навіщо викликати random.seed(...)? У яких ситуаціях потрібні однакові
   «випадкові» числа при кожному запуску?
7. Чому для роботи з таблицею (CSV) зазвичай зручніше pandas, ніж ручне
   читання файлу через split(",")? Що з цього ви вже робили вручну раніше?
"""


# %% ========== БЛОК 2. РОЗБІР БАЗОВИХ ЗАВДАНЬ (15 хв) ==========

# ---------- Приклад 1 — вбудовані бібліотеки: math, random, datetime ----------
import math
import random
from datetime import date, timedelta

random.seed(3)
radii = [random.randint(1, 10) for _ in range(4)]
areas = [round(math.pi * r ** 2, 1) for r in radii]
print(radii)
print(areas)
print(random.choice(["red", "green", "blue"]))

start = date(2024, 12, 1)
deadline = date(2024, 12, 20)
print((deadline - start).days)
print(start + timedelta(days=45))
print(deadline.strftime("%d.%m.%Y"))
print(deadline.strftime("%A"))

# Питання:
# 1. Що виведе кожен print? Запустіть код двічі: чому «випадкові» числа
#    однакові? Що зміниться, якщо прибрати random.seed(3)?
# 2. Чому ми пишемо math.pi, а не просто pi? Як переписати імпорт, щоб
#    можна було писати sqrt(...) і pi без префікса?
# 3. Яким буде тип результату (deadline - start) і що означає .days?
#    Чому start + timedelta(days=45) працює, а start + 45 — ні?


# %% ---------- Приклад 2 — власний модуль і __name__ ----------
# Файл class_utils.py лежить поруч. Відкрийте його і подивіться на код.
import class_utils as cu
from class_utils import grade

scores = [92, 75, 88, 60, 55]
print(cu.average(scores))
print([grade(s) for s in scores])
print(cu.__name__)
print(__name__)

# Питання:
# 1. Що виведе код? Чому під час імпорту НЕ з'явився текст
#    "class_utils self-test", який є в class_utils.py?
# 2. Запустіть у терміналі `python class_utils.py`. Що виведеться і чому
#    цього разу блок під if __name__ == "__main__" виконався?
# 3. Що станеться, якщо перенести class_utils.py в іншу папку? Яка помилка
#    виникне і чому?


# %% ---------- Приклад 3 — pandas і matplotlib ----------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("class_scores.csv")
print(df.shape)
print(df.groupby("group")["math"].mean().round(1))
print(df[df["python"] >= 85][["name", "python"]])

avg_math = df.groupby("group")["math"].mean()
plt.bar(avg_math.index, avg_math.values)
plt.title("Average math by group")
plt.savefig("avg_math.png")

# Питання:
# 1. Що виведе кожен print і що означає shape (10, 4)?
# 2. Що робить groupby("group")["math"].mean() — опишіть словами. Який тип
#    має результат і чому в нього є .index та .values?
# 3. Чим у рядку df[df["python"] >= 85] внутрішній вираз відрізняється від
#    зовнішнього? Чим savefig відрізняється від show()?


# %% ========== БЛОК 3. ДЕБАГІНГ (10 хв) ==========
# У кожному фрагменті є помилка. Знайдіть її та поясніть, як виправити.

# ---------- Завдання 3.1 ----------
import random

names = ["Olha", "Ivan", "Anna"]
shuffled = random.shuffle(names)
print(shuffled[0])

# Питання: яка помилка виникне і чому? Що саме повертає random.shuffle?
# Запропонуйте два способи отримати перемішаний список.


# %% ---------- Завдання 3.2 ----------
from datetime import datetime

d = datetime.strptime("17.05.2025", "%Y-%m-%d")
print(d.strftime("%d.%m.%Y"))

# Питання: що означає повідомлення про помилку? Який шаблон потрібно
# передати в strptime, щоб розібрати цей рядок? Чим strptime відрізняється
# від strftime?


# %% ---------- Завдання 3.3 ----------
import pandas as pd

df = pd.read_csv("class_scores.csv")
print(df["Math"].mean())

# Питання: яка помилка виникне і чому? Як швидко подивитися, які колонки
# є в таблиці? Як виправити код (очікується число 77.4)?


# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

# ---------- Завдання 4.1 (просте) — math і datetime ----------
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
    # TODO
    pass


def days_until(deadline, today):
    # TODO
    pass


print(circle_stats(5))                           # очікується: {'area': 78.54, 'circumference': 31.42}
print(circle_stats(1))                           # очікується: {'area': 3.14, 'circumference': 6.28}
print(days_until("20.12.2024", "01.12.2024"))    # очікується: 19
print(days_until("01.12.2024", "20.12.2024"))    # очікується: -19
print(days_until("15.03.2024", "15.03.2024"))    # очікується: 0


# %% ---------- Завдання 4.2 (середнє) — власний модуль ----------
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


# %% ---------- Завдання 4.3 (потрібен інтернет) — requests ----------
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
    # TODO
    pass


print(get_todo_title(1))
print(get_todo_title(99999))
