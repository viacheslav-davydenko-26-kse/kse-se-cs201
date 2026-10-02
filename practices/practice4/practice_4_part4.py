# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

print("# ---------- Завдання 4.1 (просте) ----------")
# Створіть словник contact із ключами "name", "phone", "email". Виведіть
# усі три значення одним f-рядком. Потім за допомогою list comprehension
# побудуйте список тих ключів словника, довжина назви яких (кількість
# символів) більша за 4.
contact = {
    "name": "Viacheslav",
    "phone": "+380123456789",
    "email": "viacheslav@kse.org.ua"
}

print(f"{contact['name']}\n{contact['phone']}\n{contact['email']}")

LENGTH_CONDITION = 4
keys = [key for key in contact.keys() if len(key) > LENGTH_CONDITION]
print(keys)


print("# ---------- Завдання 4.2 (середнє) ----------")
# Створіть словник prices, де ключі — назви товарів, а значення — їхні
# ціни (мінімум 5 пар). За допомогою list comprehension і методу
# .items() побудуйте список назв лише тих товарів, ціна яких перевищує
# 100.
prices = {
    "Product1": 100,
    "Product2": 200,
    "Product3": 300,
    "Product4": 400,
    "Product5": 500,
}

PRICE_CONDITION = 100
products = [product for product, price in prices.items() if price > PRICE_CONDITION]
print(products)


print("# ---------- Завдання 4.3 (складніше) ----------")
# Створіть словник student_scores, де ключі — імена студентів, а
# значення — їхні бали за тест (мінімум 5 пар). Обчисліть середній бал
# по групі через sum() і len() від values(). За допомогою list
# comprehension побудуйте список імен студентів, чий бал вищий за цей
# середній.
student_scores = {
    "Student1": 34,
    "Student2": 99,
    "Student3": 44,
    "Student4": 50,
    "Student5": 10,
}

average_score = sum(student_scores.values()) / len(student_scores.values())
students_filtered = [student for student, score in student_scores.items() if score > average_score]

print(students_filtered)

