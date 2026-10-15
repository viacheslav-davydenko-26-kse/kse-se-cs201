# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

# ---------- Завдання 4.1 (просте) ----------
# Напишіть функцію calculate_total(price, quantity, discount_percent=0),
# яка повертає (return) вартість покупки: ціна * кількість, зменшена
# на discount_percent відсотків. Результат округліть до 2 знаків після
# коми через round().
def calculate_total(price, quantity, discount_percent=0):
    total = price * quantity
    discount_price = total * (discount_percent / 100)
    return round(total - discount_price, 2)


print(calculate_total(50, 3))                                       # очікується: 150.0
print(calculate_total(50, 3, 10))                                   # очікується: 135.0
print(calculate_total(price=20, quantity=2, discount_percent=50))   # очікується: 20.0


# ---------- Завдання 4.2 (середнє) ----------
# Напишіть дві функції:
#
# а) count_above(threshold, *numbers) — повертає, скільки з переданих
#    чисел більші за threshold. Якщо чисел немає — поверніть 0.
#
# б) format_profile(**info) — повертає один рядок виду "ключ=значення",
#    де пари розділені символами "; " у тому порядку, в якому їх
#    передали. Функція нічого не виводить на екран, а лише повертає рядок.
def count_above(threshold, *numbers):
    return len([n for n in numbers if n > threshold])


def format_profile(**info):
    result = []
    for key, value in info.items():
        result.append(f"{key}={value}")
    return "; ".join(result)


print(count_above(10, 3, 15, 22, 7))            # очікується: 2
print(count_above(100))                         # очікується: 0
print(format_profile(name="Оля", age=18))       # очікується: name=Оля; age=18


# ---------- Завдання 4.3 (складніше) ----------
# Нижче той самий код тричі скопійовано для трьох студентів. Перепишіть
# його за принципом DRY (Don't Repeat Yourself):
#
#   1) Напишіть функцію get_status(name: str, grades: list) -> str,
#      яка рахує середнє по списку grades і ПОВЕРТАЄ рядок "<name>: <статус>".
#      Статус: середнє >= 90 — "відмінно", >= 75 — "добре",
#      інакше — "потрібно підтягнути".
#      Функція має бути чистою: без print() і без змінних поза функцією.
#   2) Викличте її для трьох студентів і виведіть результати.
#   3) Видаліть старий код, що повторюється. Вивід має залишитись таким самим.
#
# Початковий код:

def get_status(name: str, grades: list) -> str:
    avg = sum(grades) / len(grades)

    status = ""
    if avg >= 90:
        status = "відмінно"
    elif avg >= 75:
        status = "добре"
    else:
        status = "потрібно підтягнути"

    return f"{name}: {status}"

name1 = "Оля"
grades_1 = [90, 85, 100]
print(get_status(name1, grades_1))

name2 = "Іван"
grades_2 = [70, 80, 75]
print(get_status(name2, grades_2))

name3 = "Петро"
grades_3 = [50, 60, 40]
print(get_status(name3, grades_3))

# TODO: ваш варіант через функцію get_status
# очікується:
# Оля: відмінно
# Іван: добре
# Петро: потрібно підтягнути
