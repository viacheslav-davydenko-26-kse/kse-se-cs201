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
