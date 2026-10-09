"""
Assignment #1 — Programming Basics

Мета роботи:
Закріпити знання з базових конструкцій мови програмування Python.

ВАЖЛИВО:
Робота виконується індивідуально та самостійно.
"""

"""
ВАЖЛИВО: Файл із готовим рішенням потрібно прикріпити на платформі у відповідному Assignment.
Назва готового файлу має бути у форматі: assignment_1_firstname_lastname.py,
де firstname та lastname — ім’я та прізвище студента саме так, як вони записані на платформі.
"""


"""
Розподіл балів:
- Задача 1 — 2 бали
- Задача 2 — 2 бали
- Задача 3 — 3 бали
- Задача 4 — 3 бали
"""

# ============================================================
# ЗАДАЧА 1. Калькулятор чайових з урахуванням знижки
# ============================================================

"""
Програма має:

1. Запитати кількість замовлених страв.
2. Запитати ціну кожної страви.
3. Запитати відсоток чайових (наприклад, 10%, 15% або 20%).
4. Розрахувати:
   - загальну вартість страв;
   - суму чайових;
   ??? вартість страв до знижки чи після?
   - загальну суму (вартість страв + чайові).
??? чому пункт 5 не перед пунктом 4?
5. Якщо загальна вартість страв перевищує $2000,
   застосувати знижку 10% ДО розрахунку чайових.
"""

# TODO: реалізуйте задачу 1 тут
DISCOUNTED_PRICE = 2000
DISCOUNT_PERCENTAGE = 10

quantity_of_dishes = 0
dishes_prices = []

quantity_of_dishes = int(input("How many dishes are there?: "))

for i in range(quantity_of_dishes):
    price = float(input(f"What is the price of the {i + 1} dish?: "))
    dishes_prices.append(price)

tip_percentage = float(input(f"Tell me the tip percentage: "))


total_dishes_cost = sum(dishes_prices)
if total_dishes_cost > DISCOUNTED_PRICE:
    total_dishes_cost -= total_dishes_cost * (DISCOUNT_PERCENTAGE / 100)

tip_amount = total_dishes_cost * (tip_percentage / 100)

total_cost = total_dishes_cost + tip_amount

# ============================================================
# ЗАДАЧА 2. Перетворення температури і статистика
# ============================================================

"""
Користувач вводить температуру у градусах Фаренгейта
для кожного дня тижня (7 днів).

Програма має:

1. Перетворити кожну температуру у градуси Цельсія.
2. Після кожного введення показати повідомлення:

   - "Холодно" — нижче 10°C
   - "Тепло" — від 10°C до 28°C
   - "Спекотно" — вище 28°C
   - "Дуже спекотно" — вище 36°C

3. Наприкінці вивести:
   - середню температуру за тиждень;
   - мінімальну температуру;
   - максимальну температуру.
"""

# TODO: реалізуйте задачу 2 тут
week_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

degrees_C_in_week = []

for day in week_days:
    degrees_F = float(input(f"Type the temperature in degrees Fahrenheit for {day}: "))
    degrees_C = (degrees_F - 32) / 1.8
    degrees_C_in_week.append(degrees_C)

    if degrees_C < 10:
        print("Холодно")
    elif degrees_C <= 28:
        print("Тепло")
    elif degrees_C <= 36:
        print("Спекотно")
    else:
        print("Дуже спекотно")

average_temperature = sum(degrees_C_in_week) / len(degrees_C_in_week)  
min_temperature = min(degrees_C_in_week)
max_temperature = max(degrees_C_in_week)

print(average_temperature)
print(min_temperature)
print(max_temperature)


# ============================================================
# ЗАДАЧА 3. MiniRPG
# ============================================================

"""
Створіть покрокову гру "MiniRPG".

Початкові умови:
- Гравець: 50 HP
- Противник: 50 HP
- Максимум 5 ходів

Дії гравця:
??? він обирає чи ці дії йдуть одна за одною?
1. Атака:
    ??? "до" включно чи ні?
   - випадкова шкода противнику від 5 до 15 HP

2. Зцілення:
   - випадкове відновлення від 5 до 10 HP

Дія противника:
??? безкінечний цикл?
- противник завжди атакує;
- випадкова шкода гравцю від 5 до 20 HP.

Кінець гри:
- гра завершується після 5 ходів;
??? це перевіряти після кожної атаки чи в кінці ходу?
- або раніше, якщо HP гравця чи противника стає <= 0;
??? а якщо один не живий?
??? потрібно вивести повідомлення?
??? а якщо однакове?
- якщо після 5 ходів обидва живі, перемагає той,
  у кого більше HP.
"""

# TODO: імпортуйте необхідний модуль
# import ...
import random

# TODO: реалізуйте задачу 3 тут
MAX_MOVES = 5
player_HP = 50
enemy_HP = 50

for i in range(MAX_MOVES):
    # 1 move
    player_attack = random.randint(5, 16)
    enemy_HP -= player_attack 

    # 2 move
    player_healing = random.randint(5, 11)
    player_HP += player_healing

    # 3 move
    enemy_attack = random.randint(5, 21)
    player_HP -= enemy_attack

    if (player_HP <= 0) or (enemy_HP <= 0):
        break

winner = "" 
if player_HP > enemy_HP:
    winner = "player"
elif enemy_HP > player_HP:
    winner = "enemy"


# ============================================================
# ЗАДАЧА 4. Привіт, банк!
# ============================================================

"""
Створіть програму, яка симулює накопичення грошей
на банківському депозиті протягом року.

Користувач вводить:
1. Щомісячну зарплату.
2. Відсоток зарплати, який буде заощаджувати.
3. Річну процентну ставку банку.

Протягом 12 місяців програма:
- визначає суму щомісячного внеску;
- додає внесок до депозиту;
- нараховує відсотки;
- виводить баланс наприкінці кожного місяця.

Після 12 місяців користувач вирішує:
- зняти заощадження;
- або залишити їх на рахунку на наступний рік.
??? і що далі?
"""

# TODO: реалізуйте задачу 4 тут
MONTH_QUANTITY = 12
deposit = 0

salary = float(input("Type your salary: ")) 
savings_percentage = float(input("Type the percentage of the salary to be saved: "))
bank_annual_interest_rate = float(input("Type the bank's annual interest rate in percent: "))
bank_monthly_interest_rate = bank_annual_interest_rate / 12

for month in range(MONTH_QUANTITY):
    monthly_contribution = salary * (savings_percentage / 100)
    deposit += monthly_contribution
    deposit += deposit * (bank_monthly_interest_rate / 100)
    print(f"Current deposit balance in month {month + 1}: {deposit}")

answer = input("Withdraw or keep the deposit for next year? (y/n)?: ")
