"""
Практична робота — Основи ООП
Теми: класи та об'єкти, конструктор __init__, наслідування, інкапсуляція,
      поліморфізм, магічні методи (__str__, __len__, __getitem__)

Структура (50 хв):
1. Питання                      — 10 хв
2. Розбір базових завдань        — 15 хв
3. Дебагінг                      — 10 хв
4. Самостійне написання коду     — 15 хв

Комірки розділені "# %%" — у VS Code / Jupyter їх можна запускати по одній.
Додаткові файли не потрібні: усе, що треба, створюється прямо в коді.
У блоці 3 помилки в коді очікувані, тому запускайте кожну комірку окремо.
"""


# %% ========== БЛОК 1. ПИТАННЯ (10 хв) ==========
"""
Концептуальні питання до студентів:

1. Чим клас відрізняється від об'єкта? Наведіть приклад класу та кількох
   об'єктів цього класу. Чи впливає зміна атрибута в одному об'єкті на інший?
2. Що таке self у методах класу? Чому цей параметр записують першим і що
   відбувається, коли ми пишемо my_dog.bark()?
3. Що робить метод __init__ і коли він викликається? Чому зручніше
   задавати атрибути в конструкторі, а не додавати їх після створення об'єкта?
4. Що таке наслідування? Як працює super().__init__(...) і що станеться, якщо
   клас-нащадок має власний __init__, але не викликає конструктор батька?
5. Що таке перевизначення (override) методу? Як воно пов'язане з поліморфізмом:
   чому цикл for item in items: item.method() працює з об'єктами різних класів?
6. Які рівні доступу є в Python (публічний, захищений _x, приватний __x)?
   Навіщо потрібна інкапсуляція і чому дані краще читати через методи?
7. Чим атрибути відрізняються від методів? Як звернутися до кожного з
   них ззовні класу? Що станеться, якщо звернутися до атрибута, якого в
   об'єкта немає?
8. Які магічні методи ви знаєте (__str__, __len__, __getitem__)? Коли
   Python викликає їх автоматично? Наведіть по одному прикладу.
"""


# %% ========== БЛОК 2. РОЗБІР БАЗОВИХ ЗАВДАНЬ (15 хв) ==========

# ---------- Приклад 1 — клас, об'єкти, методи, __str__ ----------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"{self.owner}: {self.balance}"


a = BankAccount("Olha", 100)
b = BankAccount("Ivan")
a.deposit(50)
print(a.withdraw(500))
print(a.withdraw(30))
b.deposit(10)
print(a)
print(b)
print(a.balance + b.balance)

# Питання:
# 1. Що виведе кожен print? Чому два об'єкти a і b мають різні баланси?
# 2. Навіщо в __init__ параметр balance=0? Що буде, якщо створити
#    BankAccount("Ivan") без другого аргумента?
# 3. Чому withdraw повертає True або False, а не друкує повідомлення?
# 4. Який метод Python викликає, коли ми пишемо print(a)? Що було б виведено,
#    якби цього методу в класі не було?


# %% ---------- Приклад 2 — наслідування, super(), поліморфізм ----------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.1

    def info(self):
        return f"{self.name}: {self.salary + self.bonus():.0f}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def bonus(self):
        return self.salary * 0.1 + self.team_size * 100


staff = [Employee("Anna", 1000), Manager("Petro", 2000, 3)]
for person in staff:
    print(person.info())
print(isinstance(staff[1], Employee), isinstance(staff[0], Manager))

# Питання:
# 1. Що виведе код? Як розраховано результат для Manager?
# 2. Метод info() є лише в Employee. Чому він працює і для Manager, і
#    чому в ньому викликається саме Manager.bonus() для менеджера?
# 3. Що робить super().__init__(name, salary) і що буде, якщо цей рядок прибрати?
# 4. Що перевіряє isinstance і чому друга перевірка повертає False?


# %% ---------- Приклад 3 — інкапсуляція і магічні методи ----------
class Playlist:
    def __init__(self, name):
        self.name = name
        self.__songs = []

    def add(self, song):
        self.__songs.append(song)

    def __len__(self):
        return len(self.__songs)

    def __getitem__(self, index):
        return self.__songs[index]

    def __str__(self):
        return f"{self.name} ({len(self)} songs)"


p = Playlist("Road")
p.add("Song A")
p.add("Song B")
print(len(p))
print(p[1])
print(p)
try:
    print(p.__songs)
except AttributeError:
    print("no access")
print(p[0])

# Питання:
# 1. Що виведе код? Який магічний метод стоїть за кожним з len(p), p[1], print(p)?
# 2. Чому p.__songs викликає помилку? Як тоді користувач класу може побачити
#    пісню з плейлиста?
# 3. Що станеться з len(p) і print(p), якщо видалити з класу методи __len__
#    та __str__? Що тоді виведе print(p)?
# 4. Яка перевага від того, що список __songs закритий, а користувач працює
#    лише через методи add, len() та []?


# %% ========== БЛОК 3. ДЕБАГІНГ (10 хв) ==========
# У кожному фрагменті є помилка. Знайдіть її та поясніть, як виправити.

# ---------- Завдання 3.1 ----------
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(amount):
        self.balance += amount


acc = Account(100)
acc.deposit(50)
print(acc.balance)

# Питання: яка помилка виникне і чому, хоча ми передали лише один аргумент?
# Що ще потрібно виправити в тілі методу, щоб код запрацював?


# %% ---------- Завдання 3.2 ----------
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed


dog = Dog("Rex", "Husky")
print(dog.breed)
print(dog.name)

# Питання: яка помилка виникне і на якому рядку? Чому атрибута name немає?
# Як виправити клас Dog?


# %% ---------- Завдання 3.3 ----------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"Point({self.x}, {self.y})")


point = Point(2, 3)
print(point)

# Питання: яка помилка виникне і чому? Що саме має робити метод __str__?
# Як виправити клас, щоб print(point) вивів Point(2, 3)?


# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

# ---------- Завдання 4.1 (просте) — клас і магічний метод ----------
# Напишіть клас Rectangle:
#   - конструктор __init__(self, width, height);
#   - метод area() — повертає площу;
#   - метод perimeter() — повертає периметр;
#   - метод is_square() — повертає True, якщо ширина дорівнює висоті;
#   - метод __str__ — повертає рядок у форматі "Rectangle 4x5".
#
# Методи area, perimeter і is_square нічого не друкують, а повертають значення.
class Rectangle:
    # TODO
    pass


r = Rectangle(4, 5)
print(r)                              # очікується: Rectangle 4x5
print(r.area())                       # очікується: 20
print(r.perimeter())                  # очікується: 18
print(r.is_square())                  # очікується: False
print(Rectangle(3, 3).is_square())    # очікується: True


# %% ---------- Завдання 4.2 (складніше) — інкапсуляція і магічні методи ----------
# Напишіть клас ShoppingCart (кошик):
#   - у конструкторі створіть ПРИВАТНИЙ словник __items (спочатку порожній):
#     ключ — назва товару, значення — ціна;
#   - add_item(name, price) — додає товар у словник;
#   - total() — повертає суму цін усіх товарів, округлену до 2 знаків;
#   - __len__ — повертає кількість товарів у кошику;
#   - __str__ — повертає рядок у форматі "Cart: 3 items, total 2.60".
# Усередині класу нічого не друкуйте. Прямий доступ cart.__items ззовні має
# викликати AttributeError (перевірте через try / except і виведіть "private").
#
# Очікується:
#   3
#   2.6
#   Cart: 3 items, total 2.60
#   Cart: 4 items, total 6.00
#   private
class ShoppingCart:
    # TODO
    pass


cart = ShoppingCart()
cart.add_item("apple", 0.5)
cart.add_item("bread", 1.2)
cart.add_item("milk", 0.9)
print(len(cart))
print(cart.total())
print(cart)
cart.add_item("tea", 3.4)
print(cart)
# Перевірка приватності (допишіть try / except):
