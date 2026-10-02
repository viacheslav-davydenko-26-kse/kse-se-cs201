# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

print("# ---------- Завдання 4.1 (просте) ----------")
# Створіть змінні: first_name, last_name, birth_year.
# Обчисліть вік як 2026 - birth_year і виведіть речення на кшталт:
# "Іван Петренко, вік: 24", використовуючи f-рядок.
first_name = "Ivan" 
last_name = "Petrenko"
birth_year = 2001
year_now = 2026

age = year_now - birth_year

print(f"{first_name} {last_name}, вік: {age}")


print("# ---------- Завдання 4.2 (середнє) ----------")
# Створіть змінну age. Створіть булеву змінну can_vote, яка перевіряє,
# чи людині є 18 років або більше. Виведіть і age, і can_vote.
age = 22
AGE_REQUIRED = 18
can_vote = age >= AGE_REQUIRED
print(age, can_vote)


print("# ---------- Завдання 4.3 (складніше) ----------")
# Напишіть програму, яка через input() запитує ціну товару та кількість
# одиниць, переводить обидва значення у потрібний тип (float для ціни,
# int для кількості), обчислює загальну суму покупки і створює булеву
# змінну is_expensive, яка перевіряє, чи загальна сума перевищує 1000.
IS_EXPENSIVE_PRICE_CONDITOIN = 100

product_price = float(input("Type product price: "))
product_quantity = int(input("Type product quantity: "))

total_price = product_price * product_quantity
is_expensive = total_price > IS_EXPENSIVE_PRICE_CONDITOIN

print(is_expensive, total_price)

