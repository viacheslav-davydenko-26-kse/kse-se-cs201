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
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        format = "{}: {} x {} = {}"
        return format.format(self.name, self.quantity, self.price, self.total())

def total_cost(products):
    return round(sum(p.total() for p in products), 2)


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
