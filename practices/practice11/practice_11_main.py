"""
Практична робота — Повторення курсу: функції, бібліотеки, симуляції
Теми: списки, словники, умови, цикли, list comprehension, винятки, функції,
      math, random, datetime, pandas, matplotlib

Структура (50 хв):
1. Питання                      — 10 хв
2. Розбір базових завдань        — 15 хв
3. Дебагінг                      — 10 хв
4. Самостійне написання коду     — 15 хв

Комірки розділені "# %%" — у VS Code / Jupyter їх можна запускати по одній.
Додаткові файли не потрібні: усі дані створюються прямо в коді.
Потрібні бібліотеки: pip install pandas matplotlib
У блоці 3 помилки в коді очікувані, тому запускайте кожну комірку окремо.
"""


# %% ========== БЛОК 1. ПИТАННЯ (10 хв) ==========
"""
Концептуальні питання до студентів:

1. Чим список відрізняється від словника? За яких умов ви оберете словник,
   а не список? Наведіть приклад даних, які природно зберігати в кожному з них.
2. Чим return відрізняється від print усередині функції? Що поверне функція,
   у якій немає return, і до чого це призведе, якщо використати її результат
   у подальших обчисленнях?
3. Як працює конструкція try / except? Чому краще вказувати конкретний тип
   помилки (наприклад, ZeroDivisionError), а не писати except без типу?
4. Порівняйте import math, from math import sqrt та import pandas as pd.
   Чому не рекомендують писати from math import *?
5. Чим вбудовані бібліотеки відрізняються від сторонніх? Навіщо потрібні
   pip, віртуальне середовище та файл requirements.txt?
6. Що таке симуляція? Чому результат симуляції з random змінюється від
   запуску до запуску і як зробити його відтворюваним? Чому одного запуску
   замало, щоб оцінити ймовірність події?
7. Чому для таблиці даних зазвичай зручніше pandas, ніж списки й словники,
   які ви обробляєте циклами? Що pandas робить за вас?
8. Яку бібліотеку ви оберете для кожної задачі і чому: а) порахувати
   кількість днів до дедлайну; б) згрупувати рядки таблиці й обчислити
   середнє; в) побудувати стовпчикову діаграму; г) отримати однакову
   послідовність «випадкових» чисел при кожному запуску?
"""


# %% ========== БЛОК 2. РОЗБІР БАЗОВИХ ЗАВДАНЬ (15 хв) ==========

# ---------- Приклад 1 — функції, random, словники, comprehension ----------
import random


def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]


def count_faces(rolls):
    counts = {}
    for r in rolls:
        counts[r] = counts.get(r, 0) + 1
    return counts


random.seed(10)
rolls = roll_dice(12)
counts = count_faces(rolls)

print(rolls)
print(counts)
print(round(sum(rolls) / len(rolls), 2))
print(max(counts, key=counts.get))
print(sorted(counts.items()))

# Питання:
# 1. Що виведе кожен print? Чому, запустивши код вдруге, ви отримаєте
#    ті самі числа? Що зміниться, якщо прибрати random.seed(10)?
# 2. Навіщо в count_faces використано counts.get(r, 0), а не counts[r]?
#    Що станеться з counts[r] += 1 для грані, яка ще не зустрічалась?
# 3. Що робить max(counts, key=counts.get) і що саме повертає?
# 4. Чому roll_dice повертає список, а не друкує його?


# %% ---------- Приклад 2 — datetime, random, цикли, умови ----------
import random
from datetime import date, timedelta

random.seed(7)
start = date(2025, 3, 1)

orders = [start + timedelta(days=random.randint(0, 10)) for _ in range(4)]
deliveries = [d + timedelta(days=random.randint(1, 4)) for d in orders]

for ordered, delivered in zip(orders, deliveries):
    days = (delivered - ordered).days
    print(ordered.strftime("%d.%m"), "->", delivered.strftime("%d.%m"), days)

slow = [(d - o).days for o, d in zip(orders, deliveries) if (d - o).days >= 3]
print(slow)
print(max(deliveries).strftime("%A"))

# Питання:
# 1. Що виведе код? Який тип має різниця (delivered - ordered) і що означає .days?
# 2. Чому order + timedelta(days=3) працює, а order + 3 — ні?
# 3. Що робить zip? Чим цей цикл зручніший за цикл з індексами range(len(...))?
# 4. Як змінити код, щоб вважати «повільними» доставки від 2 днів? Що станеться
#    зі списком slow, якщо в симуляції не буде жодної такої доставки?


# %% ---------- Приклад 3 — pandas і matplotlib ----------
import random
import pandas as pd
import matplotlib.pyplot as plt

random.seed(1)
df = pd.DataFrame({
    "team": random.choices(["Red", "Blue", "Green"], k=8),
    "score": [random.randint(0, 100) for _ in range(8)],
})

print(df)
print(df.groupby("team")["score"].mean().round(1).to_dict())
print(df[df["score"] > 70])
print(len(df[df["score"] > 70]))
print(df["score"].max(), df.loc[df["score"].idxmax(), "team"])

avg = df.groupby("team")["score"].mean()
plt.bar(avg.index, avg.values)
plt.title("Average score by team")
plt.xlabel("Team")
plt.ylabel("Score")
plt.show()

# Питання:
# 1. Що виведе кожен print? Що означає кожен рядок таблиці й кожна колонка?
# 2. Що робить groupby("team")["score"].mean() — опишіть словами. Який тип
#    має результат і чому в нього є .index та .values?
# 3. Чим внутрішній вираз df["score"] > 70 відрізняється від зовнішнього
#    df[...]? Що повертає кожен із них?
# 4. Що робить idxmax і чим df.loc[...] відрізняється від звичайного
#    доступу за індексом списку?


# %% ========== БЛОК 3. ДЕБАГІНГ (10 хв) ==========
# У кожному фрагменті є помилка. Знайдіть її та поясніть, як виправити.

# ---------- Завдання 3.1 ----------
import random

random.seed(1)
items = ["a", "b", "c"]
for _ in range(6):
    print(items[random.randint(0, len(items))])

# Питання: яка помилка виникне і чому саме не одразу, а після кількох
# успішних ітерацій? Чим random.randint відрізняється від range щодо межі
# діапазону? Запропонуйте два способи виправити код.


# %% ---------- Завдання 3.2 ----------
import math


def safe_sqrt(x):
    try:
        return math.sqrt(x)
    except ZeroDivisionError:
        return None


print(safe_sqrt(9))
print(safe_sqrt(-4))

# Питання: яка помилка виникне і чому блок except її не перехопив?
# Як виправити функцію, щоб safe_sqrt(-4) повертала None?


# %% ---------- Завдання 3.3 ----------
import pandas as pd

df = pd.DataFrame({"team": ["Red", "Blue", "Red"], "score": [80, 50, 65]})
print(df[df["score"] > 60 and df["team"] == "Red"])

# Питання: що означає повідомлення про помилку? Чим логічний оператор and
# відрізняється від оператора & у pandas? Як виправити код, щоб отримати
# лише рядки команди Red зі score більшим за 60?


# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

# ---------- Завдання 4.1 (просте) — функції, random, винятки ----------
# Напишіть дві функції:
#
# а) roll_dice(n, seed) — задає random.seed(seed) і повертає список із n
#    «кидків кубика» (цілі числа від 1 до 6 включно).
#
# б) average(values) — повертає середнє значення списку, округлене до 2 знаків.
#    Для порожнього списку поверніть 0.0, обробивши ZeroDivisionError через
#    try / except (без попередньої перевірки if).
#
# Функції не мають нічого друкувати.
import random


def roll_dice(n, seed):
    # TODO
    pass


def average(values):
    # TODO
    pass


print(roll_dice(5, 1))                      # очікується: [2, 5, 1, 3, 1]
print(roll_dice(8, 42))                     # очікується: [6, 1, 1, 6, 3, 2, 2, 2]
print(average(roll_dice(10, 42)))           # очікується: 3.0
print(average([2, 3]))                      # очікується: 2.5
print(average([]))                          # очікується: 0.0


# %% ---------- Завдання 4.2 (середнє) — симуляції ----------
# а) Напишіть функцію estimate_probability(trials, seed), яка оцінює
#    ймовірність того, що сума двох кубиків дорівнює 7. Задайте random.seed(seed),
#    виконайте trials експериментів (по два кидки random.randint(1, 6)) і
#    поверніть частку успішних, округлену до 3 знаків. Для trials = 0 поверніть
#    0.0 (обробіть ZeroDivisionError через try / except).
#
# б) Напишіть функцію random_walk(steps, seed), яка імітує «блукання»:
#    стартова позиція 0, на кожному кроці позиція збільшується або зменшується
#    на 1 (random.choice([-1, 1])). Поверніть список усіх позицій, включно зі
#    стартовою (довжина steps + 1). Використайте random.seed(seed).
#
# Очікується:
#   print(estimate_probability(1000, 1))        # 0.168
#   print(estimate_probability(100000, 1))      # 0.166
#   print(estimate_probability(0, 1))           # 0.0
#   print(random_walk(10, 3))                   # [0, -1, -2, -1, 0, -1, -2, -1, 0, -1, -2]
#   print(len(random_walk(100, 5)))             # 101
#   print(random_walk(1000, 3)[-1])             # 4
# Ваш код тут:
import random


# %% ---------- Завдання 4.3 (складніше) — pandas + matplotlib ----------
# Нижче симуляція гри: троє гравців роблять по 5 раундів, у кожному раунді
# кидають два кубики, а score — сума очок. Дані вже створено — просто запустіть.
import random
import pandas as pd
import matplotlib.pyplot as plt

random.seed(2025)
rows = []
for player in ["Anna", "Ivan", "Olha"]:
    for round_no in range(1, 6):
        score = random.randint(1, 6) + random.randint(1, 6)
        rows.append({"player": player, "round": round_no, "score": score})
df = pd.DataFrame(rows)

# а) Виведіть розмір таблиці (df.shape).
# б) Порахуйте середній score кожного гравця (groupby), округліть до 2 знаків
#    і виведіть як словник (.to_dict()).
# в) Знайдіть раунд із найбільшим score і виведіть у форматі:
#    Best: <гравець> round <номер> (<score>)
#    (якщо таких кілька — візьміть перший).
# г) Виведіть, скільки раундів мали score не менше 10.
# д) Побудуйте стовпчикову діаграму середніх балів гравців із заголовком і
#    підписами осей та покажіть її через plt.show().
#
# Очікується:
#   (15, 3)
#   {'Anna': 7.2, 'Ivan': 4.2, 'Olha': 5.4}
#   Best: Anna round 2 (10)
#   2
# Ваш код тут:
