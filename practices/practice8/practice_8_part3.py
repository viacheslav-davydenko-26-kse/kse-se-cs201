# %% ========== БЛОК 3. ДЕБАГІНГ (10 хв) ==========
# У кожному фрагменті є помилка. Знайдіть її та поясніть, як виправити.

# ---------- Завдання 3.1 ----------
def add_numbers(a, b):
    return a + b

total = add_numbers(3, 4)
print(total)


# Питання: яка помилка виникне і чому? Як змінити код, не змінюючи
# саму функцію add_numbers?


# %% ---------- Завдання 3.2 ----------
def calculate_discount(price, percent):
    discount = price * percent / 100
    return price - discount


final_price = calculate_discount(200, 10)
print(final_price + 5)

# Питання: яка помилка виникне і що поверне calculate_discount? Що
# потрібно виправити у функції, щоб код дав 185.0?


# %% ---------- Завдання 3.3 ----------
counter = 0


def register_call():
    counter += 1


register_call()
register_call()
print(counter)
