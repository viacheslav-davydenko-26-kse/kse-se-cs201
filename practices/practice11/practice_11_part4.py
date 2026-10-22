# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

print("# ---------- Завдання 4.1 (просте) — функції, random, винятки ----------")
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
    random.seed(seed) 
    return [random.randint(1, 6) for _ in range(n)]


def average(values):
    try:
        return round(sum(values) / len(values), 2)
    except ZeroDivisionError:
        return 0.0



print(roll_dice(5, 1))                      # очікується: [2, 5, 1, 3, 1]
print(roll_dice(8, 42))                     # очікується: [6, 1, 1, 6, 3, 2, 2, 2]
print(average(roll_dice(10, 42)))           # очікується: 3.0
print(average([2, 3]))                      # очікується: 2.5
print(average([]))                          # очікується: 0.0


print("# %% ---------- Завдання 4.2 (середнє) — симуляції ----------")
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


print("# %% ---------- Завдання 4.3 (складніше) — pandas + matplotlib ----------")
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
