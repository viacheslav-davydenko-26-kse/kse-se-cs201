# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

print("# ---------- Завдання 4.1 (просте) — клас і магічний метод ----------")
# Напишіть клас Rectangle:
#   - конструктор __init__(self, width, height);
#   - метод area() — повертає площу;
#   - метод perimeter() — повертає периметр;
#   - метод is_square() — повертає True, якщо ширина дорівнює висоті;
#   - метод __str__ — повертає рядок у форматі "Rectangle 4x5".
#
# Методи area, perimeter і is_square нічого не друкують, а повертають значення.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}" 


r = Rectangle(4, 5)
print(r)                              # очікується: Rectangle 4x5
print(r.area())                       # очікується: 20
print(r.perimeter())                  # очікується: 18
print(r.is_square())                  # очікується: False
print(Rectangle(3, 3).is_square())    # очікується: True


print("# %% ---------- Завдання 4.2 (складніше) — інкапсуляція і магічні методи ----------")
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
    def __init__(self):
        self.__items = {}

    def add_item(self, name, price):
        self.__items[name] = price

    def total(self):
        return round(sum(self.__items.values()), 2)

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return f"Cart: {self.__len__()} items, total {self.total()}"
    

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
try:
    print(cart.__items)
except AttributeError:
    print("private")
