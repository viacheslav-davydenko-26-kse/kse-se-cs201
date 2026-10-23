"""
Домашня робота — Бібліотеки в Python
Теми: math, random, datetime, створення власних модулів, pandas, matplotlib, requests

Завдань: 20
    1–10   прості   (10 завдань)
    11–17  середні  (7 завдань)
    18–20  складні  (3 завдання)

Як працювати:
1. Покладіть цей файл і файли lib_scores.csv, lib_sales.csv, lib_weather.csv
   в одну папку. У цій же папці створюйте власні модулі (my_utils.py тощо).
2. Встановіть бібліотеки (один раз):
       pip install pandas matplotlib requests
3. Комірки розділені "# %%" — у VS Code / Jupyter їх можна запускати по одній.
   Під кожним завданням у коментарях написано очікуваний результат.
4. Завдання 10, 17 і 19 потребують інтернету.
5. Графіки зберігайте у файл (plt.savefig). За бажанням додайте plt.show().

Про очікуваний результат:
- У завданнях з random обов'язково викликайте random.seed(...) так, як написано,
  інакше числа будуть іншими. Результат перевірено на Python 3.13.
- Вивід таблиць pandas може трохи відрізнятися пробілами — важливі самі значення.
"""


# %% ========== ПРОСТІ ЗАВДАННЯ (1–10) ==========

print("# ---------- Завдання 1 (просте) — math ----------")
# Радіус кола дорівнює 5. Використайте math.pi і виведіть:
#   - площу кола (pi * r^2), округлену до 2 знаків;
#   - довжину кола (2 * pi * r), округлену до 2 знаків;
#   - площу, округлену вгору (math.ceil);
#   - площу, округлену вниз (math.floor).
#
# Очікується:
#   Area: 78.54
#   Circumference: 31.42
#   Ceil: 79
#   Floor: 78
import math

radius = 5
# Ваш код тут:
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))
print("Ceil:", math.ceil(area))
print("Floor:", math.floor(area))


print("# %% ---------- Завдання 2 (просте) — math ----------")
# Виведіть за допомогою функцій модуля math:
#   - факторіал числа 6;
#   - найбільший спільний дільник чисел 48 і 36 (math.gcd);
#   - найменше спільне кратне чисел 4 і 6 (math.lcm);
#   - квадратний корінь із 144 (math.sqrt);
#   - 2 у степені 10 через math.pow.
# Зверніть увагу: math.sqrt і math.pow повертають float.
#
# Очікується:
#   Factorial of 6: 720
#   GCD(48, 36): 12
#   LCM(4, 6): 12
#   Square root of 144: 12.0
#   Power 2^10: 1024.0
import math

# Ваш код тут:
print("Factorial of 6:", math.factorial(6))
print("GCD(48, 36):", math.gcd(48, 36))
print("LCM(4, 6):", math.lcm(4, 6))
print("Square root of 144:", math.sqrt(144))
print("Power 2^10:", math.pow(2, 10))


print("# %% ---------- Завдання 3 (просте) — random ----------")
# Викличте random.seed(42). Створіть список із 5 випадкових цілих чисел
# від 1 до 100 (random.randint) і виведіть сам список, його мінімум,
# максимум і суму.
#
# Очікується:
#   Numbers: [82, 15, 4, 95, 36]
#   Min: 4
#   Max: 95
#   Sum: 232
import random

random.seed(42)
# Ваш код тут:
random_list = [random.randint(1, 100) for _ in range(5)]

print("Numbers:", random_list)
print("Min:", min(random_list))
print("Max:", max(random_list))
print("Sum:", sum(random_list))

print("# %% ---------- Завдання 4 (просте) — random ----------")
# Викличте random.seed(7). Дано список імен. У такому порядку:
#   1) виберіть переможця через random.choice;
#   2) зробіть копію списку (names[:]) і перемішайте її через random.shuffle;
#   3) виведіть вихідний список (він не повинен змінитися);
#   4) виберіть команду з 2 людей через random.sample.
#
# Очікується:
#   Winner: Anna
#   Shuffled: ['Sofia', 'Olha', 'Anna', 'Taras', 'Ivan']
#   Original: ['Olha', 'Ivan', 'Anna', 'Taras', 'Sofia']
#   Team: ['Olha', 'Sofia']
import random

random.seed(7)
names = ["Olha", "Ivan", "Anna", "Taras", "Sofia"]
# Ваш код тут:

print("Winner:", random.choice(names))
names_shuffled = names[:]
random.shuffle(names_shuffled)
print("Shuffled:", names_shuffled)
print("Original:", names)
print("Team:", random.sample(names, 2))

print("# %% ---------- Завдання 5 (просте) — datetime ----------")
# Створіть дату 29 лютого 2024 року (datetime.date) і виведіть:
#   - дату у форматі ISO (print(d));
#   - назву дня тижня англійською (strftime("%A"));
#   - дату у форматі дд.мм.рррр (strftime("%d.%m.%Y"));
#   - рік, місяць і день одним рядком через пробіл.
#
# Очікується:
#   ISO: 2024-02-29
#   Weekday: Thursday
#   Formatted: 29.02.2024
#   Year/Month/Day: 2024 2 29
from datetime import date

# Ваш код тут:
my_date = date(day=29, month=2, year=2024)
print("ISO:", my_date)
print("Weekday:", my_date.strftime("%A"))
print("Formatted:", my_date.strftime("%d.%m.%Y"))
print("Year/Month/Day:", my_date.year, my_date.month, my_date.day)


# %% ---------- Завдання 6 (просте) — datetime ----------
# Дано дати start = 1 вересня 2024 і end = 20 грудня 2024.
# Виведіть:
#   - скільки днів між ними (різниця дат дає timedelta, у неї є .days);
#   - дату через 100 днів після start;
#   - дату за 30 днів до start.
# Використайте datetime.timedelta.
#
# Очікується:
#   Days between: 110
#   100 days after start: 2024-12-10
#   30 days before start: 2024-08-02
from datetime import date, timedelta

start = date(2024, 9, 1)
end = date(2024, 12, 20)
# Ваш код тут:


# %% ---------- Завдання 7 (просте) — власний модуль ----------
# а) Створіть у цій же папці файл my_utils.py з таким вмістом:
#      - константа VERSION = "1.0";
#      - функція square(n)      — повертає n * n;
#      - функція is_even(n)     — повертає True, якщо n парне;
#      - функція greet(name)    — повертає рядок "Hello, <name>!".
# б) Тут імпортуйте модуль двома способами:
#      import my_utils
#      from my_utils import greet as hello
#    і виведіть результати.
#
# Очікується:
#   49            <- my_utils.square(7)
#   True          <- my_utils.is_even(10)
#   Hello, Olha!  <- hello("Olha")
#   1.0           <- my_utils.VERSION
# Ваш код тут (імпорт і виклики):


# %% ---------- Завдання 8 (просте) — pandas ----------
# Файл lib_scores.csv має колонки name, age, score.
# Прочитайте його через pd.read_csv і виведіть:
#   - розмір таблиці (df.shape);
#   - список назв колонок;
#   - середній бал (колонка score);
#   - ім'я студента з найвищим балом (idxmax + loc);
#   - перші 3 рядки (df.head(3)).
#
# Очікується:
#   Shape: (8, 3)
#   Columns: ['name', 'age', 'score']
#   Mean score: 77.25
#   Best student: Sofia
#      name  age  score
#   0  Olha   19     92
#   1  Ivan   20     75
#   2  Anna   19     88
import pandas as pd

# Ваш код тут:


# %% ---------- Завдання 9 (просте) — matplotlib ----------
# Побудуйте лінійний графік: x = числа від 1 до 10, y = квадрати цих чисел.
# Додайте маркери (marker="o"), заголовок "Squares", підписи осей ("n" та
# "n squared") і сітку. Збережіть графік у файл squares.png, потім виведіть
# повідомлення і перевірте, що файл існує (os.path.exists).
#
# Очікується:
#   Saved: squares.png
#   File exists: True
# (і файл squares.png з графіком у вашій папці)
import os
import matplotlib.pyplot as plt

# Ваш код тут:


# %% ---------- Завдання 10 (просте) — requests ----------
# Зробіть GET-запит на https://jsonplaceholder.typicode.com/todos/1
# (параметр timeout=10). Виведіть:
#   - код відповіді (response.status_code);
#   - поле "title" з JSON (response.json());
#   - поле "completed".
#
# Очікується:
#   200
#   delectus aut autem
#   False
import requests

# Ваш код тут:


# %% ========== СЕРЕДНІ ЗАВДАННЯ (11–17) ==========

# ---------- Завдання 11 (середнє) — math ----------
# а) Напишіть функцію solve_quadratic(a, b, c) для рівняння ax^2 + bx + c = 0.
#    Використайте дискримінант і math.sqrt. Функція повертає кортеж коренів,
#    округлених до 2 знаків, за зростанням:
#      D > 0  -> два корені (x1, x2), x1 < x2;
#      D == 0 -> один корінь (x,);
#      D < 0  -> порожній кортеж ().
#    Якщо a == 0 — викличте raise ValueError("a must not be 0").
#
# б) Напишіть функцію nearest_to_origin(points), яка отримує список точок
#    (кортежів (x, y)) і повертає точку, найближчу до (0, 0).
#    Використайте math.dist і min(..., key=...).
#
# Очікується:
#   print(solve_quadratic(1, -3, 2))     # (1.0, 2.0)
#   print(solve_quadratic(1, 2, 1))      # (-1.0,)
#   print(solve_quadratic(1, 0, 1))      # ()
#   print(solve_quadratic(2, -4, -6))    # (-1.0, 3.0)
#   print(solve_quadratic(1, 1, -1))     # (-1.62, 0.62)
#   solve_quadratic(0, 2, 1) -> try/except виводить: Error: a must not be 0
#   print(nearest_to_origin([(3, 4), (1, 1), (-2, 0)]))   # (1, 1)
import math


def solve_quadratic(a, b, c):
    # TODO
    pass


def nearest_to_origin(points):
    # TODO
    pass


print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 1))
print(solve_quadratic(1, 0, 1))
print(solve_quadratic(2, -4, -6))
print(solve_quadratic(1, 1, -1))
# TODO: викличте solve_quadratic(0, 2, 1) у try/except і виведіть "Error: ..."
print(nearest_to_origin([(3, 4), (1, 1), (-2, 0)]))


# %% ---------- Завдання 12 (середнє) — random ----------
# Симуляція кидання кубика.
# а) roll_dice(n) — повертає список із n результатів кидків (random.randint(1, 6)).
# б) count_faces(rolls) — повертає словник {грань: скільки разів випала}
#    для ВСІХ граней 1..6 (навіть якщо якась не випала — тоді 0).
# в) Викличте random.seed(1), киньте кубик 600 разів, виведіть словник,
#    грань, що випала найчастіше (за рівності — менша грань), і суму значень
#    словника (має бути 600).
#
# Очікується:
#   {1: 104, 2: 102, 3: 103, 4: 94, 5: 113, 6: 84}
#   Most frequent: 5 (113 times)
#   Total: 600
import random


def roll_dice(n):
    # TODO
    pass


def count_faces(rolls):
    # TODO
    pass


random.seed(1)
# Ваш код тут (кидки, підрахунок, вивід):


# %% ---------- Завдання 13 (середнє) — datetime ----------
# Дати подано рядками у форматі "дд.мм.рррр" (datetime.strptime(s, "%d.%m.%Y")).
# а) days_until_birthday(birthday, today) — скільки днів залишилось до
#    наступного дня народження. Якщо день народження сьогодні — 0.
#    Якщо цього року він уже минув — рахуйте до наступного року.
#    (Для 29 лютого в невисокосний рік вважайте днем народження 1 березня —
#    це необов'язково, у тестах такого немає.)
# б) age_on(birthday, today) — скільки повних років виповнилось на дату today.
#
# Очікується:
#   print(days_until_birthday("15.03.2005", "10.03.2024"))   # 5
#   print(days_until_birthday("15.03.2005", "15.03.2024"))   # 0
#   print(days_until_birthday("15.03.2005", "16.03.2024"))   # 364
#   print(days_until_birthday("01.01.2000", "31.12.2024"))   # 1
#   print(age_on("15.03.2005", "14.03.2024"))                # 18
#   print(age_on("15.03.2005", "15.03.2024"))                # 19
from datetime import datetime, date, timedelta


def days_until_birthday(birthday, today):
    # TODO
    pass


def age_on(birthday, today):
    # TODO
    pass


print(days_until_birthday("15.03.2005", "10.03.2024"))
print(days_until_birthday("15.03.2005", "15.03.2024"))
print(days_until_birthday("15.03.2005", "16.03.2024"))
print(days_until_birthday("01.01.2000", "31.12.2024"))
print(age_on("15.03.2005", "14.03.2024"))
print(age_on("15.03.2005", "15.03.2024"))


# %% ---------- Завдання 14 (середнє) — власний модуль і __name__ ----------
# а) Створіть файл geometry.py з функціями (кожна — з docstring):
#      circle_area(radius)          — площа кола, округлена до 2 знаків
#                                     (docstring: "Return the area of a circle.");
#      rectangle_area(width, height);
#      triangle_area(base, height)  — base * height / 2.
#    Усередині модуля використайте math.pi.
# б) Наприкінці geometry.py додайте блок
#        if __name__ == "__main__":
#            ...
#    який друкує "Running geometry.py directly" і демонстраційні виклики:
#    circle_area(1), rectangle_area(2, 3), triangle_area(4, 5).
#    Запустіть у терміналі `python geometry.py` і переконайтесь, що він
#    працює (виведе: Running geometry.py directly, 3.14, 6, 10.0).
# в) Тут імпортуйте модуль трьома способами (import geometry,
#    from geometry import circle_area as ca, import geometry as geo) і
#    виведіть результати. Важливо: під час імпорту текст
#    "Running geometry.py directly" з'являтись НЕ повинен.
#
# Очікується:
#   geometry                          <- geometry.__name__
#   78.54                             <- ca(5)
#   24                                <- geo.rectangle_area(4, 6)
#   6.0                               <- geometry.triangle_area(3, 4)
#   Return the area of a circle.      <- geometry.circle_area.__doc__
# Ваш код тут (імпорт і виклики):


# %% ---------- Завдання 15 (середнє) — pandas ----------
# Файл lib_sales.csv: date, category, product, quantity, price.
# а) Додайте колонку total = quantity * price.
# б) Порахуйте виручку по кожній категорії (groupby + sum), округліть до
#    2 знаків і відсортуйте за спаданням.
# в) Виведіть назви товарів і total для рядків, де total > 20.
# г) Виведіть кількість унікальних товарів (nunique).
#
# Очікується:
#   category
#   Dairy     61.0
#   Bakery    57.9
#   Fruits    47.9
#   Name: total, dtype: float64
#     product  total
#   4  Cheese   22.5
#   Unique products: 9
import pandas as pd

sales = pd.read_csv("lib_sales.csv")
# Ваш код тут:


# %% ---------- Завдання 16 (середнє) — matplotlib ----------
# Використайте виручку по категоріях із завдання 15 (змінна revenue — Series
# або ваш аналог). Створіть фігуру з двома графіками поруч
# (fig, axes = plt.subplots(1, 2, figsize=(10, 4))):
#   - ліворуч — стовпчикова діаграма (bar) з заголовком "Revenue by category",
#     підписами осей та значеннями над стовпчиками (ax.bar_label);
#   - праворуч — кругова діаграма (pie) з відсотками (autopct) і
#     заголовком "Share of revenue".
# Збережіть фігуру у revenue_by_category.png і виведіть, чи файл не порожній
# (os.path.getsize(...) > 0).
#
# Очікується:
#   Chart saved: True
import os
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("lib_sales.csv")
sales["total"] = sales["quantity"] * sales["price"]
revenue = sales.groupby("category")["total"].sum().round(2).sort_values(ascending=False)
# Ваш код тут:


# %% ---------- Завдання 17 (середнє) — requests ----------
# Працюємо з тестовим API https://jsonplaceholder.typicode.com
# а) get_user_name(user_id) — робить GET на /users/<user_id>, перевіряє
#    успішність через response.raise_for_status() і повертає поле "name".
#    Якщо сталась будь-яка помилка requests (requests.exceptions.RequestException,
#    зокрема HTTPError для 404) — повертає None.
# б) get_user_posts(user_id) — робить GET на /posts з параметром
#    params={"userId": user_id} і повертає список постів (список словників).
#    У разі помилки повертає порожній список [].
#    Обидва запити — з timeout=10.
#
# Очікується:
#   User: Leanne Graham
#   Posts: 10
#   First title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
#   User 999: None
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user_name(user_id):
    # TODO
    pass


def get_user_posts(user_id):
    # TODO
    pass


posts = get_user_posts(1)
print("User:", get_user_name(1))
print("Posts:", len(posts))
print("First title:", posts[0]["title"])
print("User 999:", get_user_name(999))


# %% ========== СКЛАДНІ ЗАВДАННЯ (18–20) ==========

# ---------- Завдання 18 (складне) — власний модуль + pandas + matplotlib ----------
# Файл lib_weather.csv: date, temp — щоденна температура з 1 січня по
# 31 березня 2024 року (91 рядок).
#
# а) Створіть модуль weather_tools.py з функціями:
#    load_weather(path)
#        читає CSV, перетворює колонку date на дати (pd.to_datetime),
#        сортує за датою, скидає індекс (reset_index(drop=True)), повертає DataFrame;
#    monthly_stats(df)
#        повертає DataFrame, де індекс — номер місяця (назва індексу "month"),
#        а колонки mean, min, max — статистика temp за місяць, округлена до
#        1 знака (groupby за df["date"].dt.month + .agg([...]));
#    hottest_day(df)
#        повертає кортеж (дата у форматі "рррр-мм-дд", температура float);
#    add_rolling_mean(df, window=7)
#        повертає НОВИЙ DataFrame (df.copy()) із додатковою колонкою
#        "rolling" — ковзне середнє temp за window днів, округлене до 1 знака.
#        Вихідний df змінювати не можна;
#    plot_temperature(df, filename)
#        будує лінію щоденної температури і, якщо в df є колонка "rolling",
#        ще й лінію ковзного середнього; додає заголовок, підписи осей,
#        легенду та сітку; зберігає в filename; нічого не повертає.
#    Додайте в кінець модуля блок if __name__ == "__main__": з коротким
#    самотестом (наприклад, друк кількості завантажених рядків).
#
# б) Тут імпортуйте модуль (import weather_tools as wt) і виведіть:
#
# Очікується:
#   Date is datetime: True
#          mean  min   max
#   month
#   1      -1.5 -7.6   3.5
#   2       0.8 -4.8   7.5
#   3       5.1 -0.5  10.8
#   ('2024-03-22', 10.8)
#   Missing rolling values: 6          <- кількість NaN у колонці rolling
#   Original has rolling: False        <- чи з'явилась rolling у вихідному df
#   Chart saved: True                  <- файл temperature.png створено
#
# Підказки: pd.api.types.is_datetime64_any_dtype(df["date"]),
#           df["temp"].rolling(window).mean(), df["rolling"].isna().sum().
# Ваш код тут (імпорт і виклики):


# %% ---------- Завдання 19 (складне) — requests + pandas + matplotlib ----------
# Аналітика задач користувачів із https://jsonplaceholder.typicode.com/todos
# (200 задач; у кожної є userId, id, title, completed).
#
# а) load_todos(cache_path="todos.csv") — завантажує задачі через requests
#    (timeout=10, raise_for_status), перетворює на pd.DataFrame, зберігає
#    копію у cache_path (to_csv(index=False)) і повертає таблицю.
#    Режим офлайн: якщо сталась помилка requests.exceptions.RequestException
#    і файл cache_path існує — повертає таблицю, прочитану з файлу;
#    якщо файлу немає — повертає порожній DataFrame().
#    (Перевірте офлайн-режим: вимкніть інтернет і запустіть ще раз.)
# б) Виведіть кількість задач, кількість унікальних користувачів та список
#    унікальних кількостей задач на користувача.
# в) Порахуйте для кожного користувача відсоток виконаних задач
#    (середнє значення колонки completed * 100, округлене до 1 знака) і
#    виведіть його, а також користувача з найвищим відсотком.
# г) Побудуйте стовпчикову діаграму «відсоток виконаних задач по
#    користувачах» (підписи осей, заголовок) і збережіть у completion_rate.png.
#
# Очікується (точні відсотки беруться з API — звіряйте лише структуру і числа,
# які тут вказані):
#   Source: API                (або "Source: cache" в офлайні)
#   Todos loaded: 200
#   Users: 10
#   Todos per user: [20]
#   userId
#   1     <відсоток>
#   ...                        (10 рядків, один на користувача)
#   10    <відсоток>
#   Name: completed, dtype: float64
#   Top user: <userId> <відсоток>
#   Chart saved: True
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "https://jsonplaceholder.typicode.com"


def load_todos(cache_path="todos.csv"):
    # TODO
    pass


# Ваш код тут (виклик, аналіз, графік):


# %% ---------- Завдання 20 (складне) — random + datetime + pandas + власний модуль ----------
# Симулятор журналу подій (лог-файлу) та його аналіз.
#
# а) Створіть модуль log_tools.py з такими елементами:
#    Константи:
#        LEVELS   = ["INFO", "WARNING", "ERROR"]
#        WEIGHTS  = [70, 20, 10]
#        MESSAGES = ["login", "logout", "upload", "download", "payment"]
#        START    = datetime(2024, 5, 1, 8, 0, 0)
#    Функції:
#    generate_log(path, n, seed)
#        створює rng = random.Random(seed) і записує у файл n рядків формату
#            2024-05-01 08:08:02 | INFO | payment
#        Для КОЖНОГО рядка у ТАКОМУ порядку:
#            1) поточний час збільшується на timedelta(seconds=rng.randint(1, 600))
#               (початковий поточний час — START; перший рядок вже має
#               збільшений час);
#            2) level = rng.choices(LEVELS, weights=WEIGHTS)[0];
#            3) message = rng.choice(MESSAGES).
#        Порядок викликів важливий: тільки так ваші числа збігуться з очікуваними.
#    parse_log(path)
#        читає файл і повертає DataFrame з колонками timestamp (datetime),
#        level, message (порожні рядки пропускає);
#    errors_per_hour(df)
#        повертає словник {година: кількість рядків рівня ERROR}, лише для
#        годин, де були помилки, за зростанням години;
#    busiest_hour(df)
#        повертає кортеж (година, кількість записів) для години з найбільшою
#        кількістю записів (за рівності — менша година);
#    longest_gap(df)
#        повертає кортеж (найбільша пауза між двома сусідніми записами як
#        timedelta, час першого запису пари, час другого запису пари).
#
# б) Тут імпортуйте модуль, згенеруйте файл app.log на 200 записів із seed=2024,
#    розберіть його і виведіть:
#
# Очікується:
#   Lines: 200
#   First: 2024-05-01 08:08:02 | INFO | payment
#   Last: 2024-05-02 01:02:05 | INFO | payment
#   {'INFO': 140, 'WARNING': 37, 'ERROR': 23}          <- кількість за рівнями
#   Busiest hour: (10, 15)
#   Errors per hour: {8: 1, 9: 1, 10: 2, 11: 4, 13: 2, 14: 1, 15: 1, 16: 1, 18: 2, 19: 1, 20: 1, 21: 2, 22: 3, 23: 1}
#   Longest gap: 0:09:58 from 2024-05-01 14:24:53 to 2024-05-01 14:34:51
#
# Підказки: df["timestamp"].dt.hour, df["timestamp"].diff(), .idxmax(),
#           .to_pytimedelta(), df["level"].value_counts().
# Ваш код тут (імпорт і виклики):
