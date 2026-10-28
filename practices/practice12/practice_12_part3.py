# %% ========== БЛОК 3. ДЕБАГІНГ (10 хв) ==========
# У кожному фрагменті є помилка. Знайдіть її та поясніть, як виправити.

print("# ---------- Завдання 3.1 ----------")
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(amount):
        self.balance += amount


acc = Account(self, 100)
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
