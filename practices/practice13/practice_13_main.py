"""
Практична робота 13 — Повторення курсу з фокусом на класи
Теми: класи та об'єкти, __init__, наслідування, інкапсуляція, магічні методи,
      функції, винятки, файли, списки та словники, random, datetime, pandas, matplotlib

Структура (50 хв):
1. Питання                      — 10 хв
2. Розбір базових завдань        — 15 хв
3. Дебагінг                      — 10 хв
4. Самостійне написання коду     — 15 хв

Комірки розділені "# %%" — у VS Code / Jupyter їх можна запускати по одній.
Додаткові файли не потрібні: усе, що треба, створюється прямо в коді.
Потрібні бібліотеки: pip install pandas matplotlib
У блоці 3 помилки в коді очікувані, тому запускайте кожну комірку окремо.
"""


# %% ========== БЛОК 1. ПИТАННЯ (10 хв) ==========
"""
Концептуальні питання до студентів:

1. Уявіть, що ви описуєте клас Student для системи курсу. Які атрибути та
   методи в нього будуть? Які з них зробите публічними, а які приватними і чому?
2. Чим метод відрізняється від звичайної функції? Для кожного випадку скажіть,
   що ви напишете — функцію чи метод класу: а) перевірити, чи число парне;
   б) зняти гроші з рахунку; в) порахувати середнє значення списку.
3. Що станеться в цьому коді: a = Account(100); b = a; b.deposit(50)?
   Чому a.balance теж змінився? Чим це відрізняється від створення двох окремих
   об'єктів Account(100)?
4. Маємо список об'єктів класу Order. Якими конструкціями ви знайдете
   найбільше замовлення, відсортуєте їх за сумою і виберете лише великі?
   Для чого тут lambda?
5. Навіщо класу метод __str__, якщо можна написати окрему функцію show(obj)?
   Що виведе print(obj) без нього?
6. Метод класу може кинути ValueError. Де краще перехоплювати помилку — у
   самому методі чи в коді, що його викликає? Як зробити, щоб один некоректний
   рядок даних не зупинив обробку решти?
7. Як перейти від списку об'єктів до таблиці pandas і до рядків у файлі?
   Які атрибути та методи ви для цього використаєте? Коли варто лишити
   список об'єктів, а коли зручніше DataFrame?
8. Чому для симуляції гри зручно описати гравця окремим класом? Де правильно
   викликати random.seed — один раз перед симуляцією чи в кожному об'єкті? Чому?
"""


# %% ========== БЛОК 2. РОЗБІР БАЗОВИХ ЗАВДАНЬ (15 хв) ==========

# ---------- Приклад 1 — клас, список об'єктів, comprehension, словник ----------
class Book:
    def __init__(self, title, author, pages, available=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available

    def borrow(self):
        if not self.available:
            return False
        self.available = False
        return True

    def __str__(self):
        status = "in" if self.available else "out"
        return f"{self.title} ({self.pages} p., {status})"


books = [
    Book("Dune", "Herbert", 600),
    Book("Emma", "Austen", 400),
    Book("Ulysses", "Joyce", 700, False),
    Book("Hamlet", "Shakespeare", 150),
]
print(books[0].borrow())
print(books[0].borrow())
print(books[2].borrow())
for b in books:
    print(b)
free = [b.title for b in books if b.available]
print(free)
by_author = {b.author: b.pages for b in books}
print(max(by_author, key=by_author.get))
print(sum(b.pages for b in books if not b.available))

# Питання:
# 1. Що виведе кожен print? Чому другий виклик books[0].borrow() повертає False?
# 2. Чому в конструкторі параметр available=True, а в Ulysses передано False?
# 3. Що робить max(by_author, key=by_author.get) і що саме він повертає?
# 4. Чому borrow повертає True або False, а не друкує повідомлення?


# %% ---------- Приклад 2 — наслідування, super() у методі, винятки, файли ----------
class Ticket:
    def __init__(self, passenger, age, base_price):
        if age < 0:
            raise ValueError("bad age")
        self.passenger = passenger
        self.age = age
        self.base_price = base_price

    def price(self):
        if self.age < 12:
            return self.base_price / 2
        return self.base_price

    def line(self):
        return f"{self.passenger}: {self.price():.0f}"


class VipTicket(Ticket):
    def __init__(self, passenger, age, base_price, meals):
        super().__init__(passenger, age, base_price)
        self.meals = meals

    def price(self):
        return super().price() + 30 * self.meals


data = [("Anna", 30, 100), ("Bob", -1, 100), ("Kid", 8, 100)]
tickets = []
for passenger, age, base in data:
    try:
        tickets.append(Ticket(passenger, age, base))
    except ValueError as e:
        print("skip", passenger, e)
tickets.append(VipTicket("Zoe", 10, 100, 2))

with open("tickets.txt", "w") as f:
    for t in tickets:
        f.write(t.line() + "\n")

with open("tickets.txt") as f:
    lines = f.read().splitlines()
print(len(lines))
print(lines)
print(sum(t.price() for t in tickets))

# Питання:
# 1. Що виведе код? Чому Bob не потрапив у файл і що саме його «відфільтрувало»?
# 2. Метод line() є лише в Ticket. Чому для Zoe він дає іншу ціну, ніж для Kid?
# 3. Що означає super().price() усередині VipTicket.price()? Що було б, якби
#    замість нього написати self.price()?
# 4. Що станеться з файлом tickets.txt, якщо замінити режим "w" на "a" і
#    запустити код двічі? Навіщо тут with?


# %% ---------- Приклад 3 — клас + random + datetime + pandas + matplotlib ----------
import random
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt


class Order:
    def __init__(self, city, amount, day):
        self.city = city
        self.amount = amount
        self.day = day

    def is_big(self):
        return self.amount >= 100


random.seed(5)
start = date(2025, 5, 1)
cities = ["Kyiv", "Lviv", "Odesa"]
orders = []
for _ in range(8):
    city = random.choice(cities)
    amount = random.randint(20, 200)
    day = start + timedelta(days=random.randint(0, 6))
    orders.append(Order(city, amount, day))

df = pd.DataFrame({
    "city": [o.city for o in orders],
    "amount": [o.amount for o in orders],
    "weekday": [o.day.strftime("%a") for o in orders],
})
print(df)
print(df.groupby("city")["amount"].sum().to_dict())
print(sum(o.is_big() for o in orders))
print(max(orders, key=lambda o: o.amount).day.strftime("%d.%m"))

totals = df.groupby("city")["amount"].sum()
plt.bar(totals.index, totals.values)
plt.title("Total amount by city")
plt.xlabel("City")
plt.ylabel("Amount")
plt.show()

# Питання:
# 1. Що виведе кожен print? Чому, запустивши код вдруге, ви отримаєте ті самі дані?
# 2. Як із списку об'єктів Order ми отримали таблицю? Що означає кожен стовпець?
# 3. Що робить sum(o.is_big() for o in orders)? Чому тут можна підсумовувати True/False?
# 4. Що робить groupby("city")["amount"].sum() — опишіть словами. Як із нього
#    отримати дані для стовпчикової діаграми?


# %% ========== БЛОК 3. ДЕБАГІНГ (10 хв) ==========
# У кожному фрагменті є помилка. Знайдіть її та поясніть, як виправити.

# ---------- Завдання 3.1 ----------
class Cat:
    def __init__(self, name, age):
        name = name
        self.age = age

    def info(self):
        return f"{self.name}, {self.age}"


cat = Cat("Tom", 3)
print(cat.info())

# Питання: яка помилка виникне і на якому рядку? Чому атрибута name немає,
# хоча ми передали його в конструктор? Як виправити клас?


# %% ---------- Завдання 3.2 ----------
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


class Savings(Account):
    def add_bonus(self):
        self.__balance += 10


s = Savings(100)
s.add_bonus()
print(s.get_balance())

# Питання: яка помилка виникне і чому клас-нащадок не бачить __balance батька?
# Запропонуйте виправлення, яке не відкриває атрибут для всіх.


# %% ---------- Завдання 3.3 ----------
class Runner:
    def __init__(self, name, score):
        self.name = name
        self.score = score


runners = [Runner("Anna", 5), Runner("Ivan", 9), Runner("Olha", 7)]
ranking = sorted(runners)
print([r.name for r in ranking])

# Питання: що означає повідомлення про помилку? Чому Python не знає, як
# порівняти два об'єкти? Як виправити виклик sorted, щоб отримати імена
# від найменшого score до найбільшого?


# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

# ---------- Завдання 4.1 (просте) — клас і функція ----------
# Напишіть клас Product:
#   - конструктор __init__(self, name, price, quantity);
#   - метод total() — повертає price * quantity, округлене до 2 знаків;
#   - метод __str__ — повертає рядок у форматі "apple: 3 x 2.50 = 7.50".
#
# Напишіть функцію total_cost(products) — приймає список об'єктів Product і
# повертає суму їхніх total(), округлену до 2 знаків. Для порожнього списку
# функція поверне 0.
#
# Методи та функція нічого не друкують, а повертають значення.
class Product:
    # TODO
    pass


def total_cost(products):
    # TODO
    pass


apple = Product("apple", 2.5, 3)
milk = Product("milk", 1.2, 2)
print(apple)                          # очікується: apple: 3 x 2.50 = 7.50
print(apple.total())                  # очікується: 7.5
print(milk)                           # очікується: milk: 2 x 1.20 = 2.40
print(total_cost([apple, milk]))      # очікується: 9.9
print(total_cost([]))                 # очікується: 0


# %% ---------- Завдання 4.2 (складніше) — клас, random і функція ----------
# Напишіть симуляцію простої гри.
#
# а) Клас Player:
#    - конструктор __init__(self, name) — зберігає ім'я та створює score = 0;
#    - метод roll() — кидає кубик (random.randint(1, 6)), додає результат до
#      score і повертає його;
#    - метод __str__ — повертає рядок у форматі "Anna: 17".
#
# б) Функція play_game(names, rounds, seed):
#    - задає random.seed(seed);
#    - створює по одному об'єкту Player для кожного імені зі списку names;
#    - виконує rounds раундів: у кожному раунді кожен гравець по черзі
#      (у порядку списку) робить один roll();
#    - повертає об'єкт гравця з найбільшим score (якщо таких кілька — першого).
#
# Усередині класу та функції нічого не друкуйте.
#
# Очікується:
#   print(play_game(["Anna", "Ivan", "Olha"], 5, 1))     # Anna: 17
#   print(play_game(["Anna", "Ivan", "Olha"], 5, 2))     # Olha: 21
#   print(play_game(["A", "B"], 10, 7))                  # B: 27
#   Повторний запуск із тим самим seed дає той самий результат:
#   print(str(play_game(["Anna", "Ivan", "Olha"], 5, 1)) == "Anna: 17")   # True
import random


class Player:
    # TODO
    pass


def play_game(names, rounds, seed):
    # TODO
    pass
