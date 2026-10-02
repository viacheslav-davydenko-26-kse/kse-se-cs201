# %% ========== БЛОК 4. САМОСТІЙНІ ЗАВДАННЯ  (15 хв) ==========

print("# ---------- Завдання 4.1 (просте) ----------")
# Створіть список favorite_numbers із трьох чисел. Створіть other_list,
# написавши other_list = favorite_numbers (без .copy() і без зрізу).
# Додайте до other_list ще одне число методом append(). Виведіть обидва
# списки.

favorite_numbers = [1, 2, 3]
other_list = favorite_numbers
other_list.append(4)
print(favorite_numbers)
print(other_list)

print("# ---------- Завдання 4.2 (середнє) ----------")
# Дано список слів: words = ["кіт", "пес", "кіт", "птах", "пес", "кіт"].
# Спочатку спробуйте найпростіший, "наївний" варіант підрахунку: створіть
# порожній словник word_counts і в циклі for напишіть
# word_counts[word] += 1 без жодних перевірок. Подивіться, яка помилка
# виникне вже на першому ж слові. Після цього перепишіть код так, щоб він
# правильно порахував, скільки разів зустрічається кожне слово
# (наприклад, за допомогою .get() з значенням за замовчуванням 0).

words = ["кіт", "пес", "кіт", "птах", "пес", "кіт"]
word_counts = {}
for word in words:
    """
    word_counts[word] += 1 
    KeyError:
    """
    word_counts[word] = word_counts.get(word, 0)
    word_counts[word] += 1
print(word_counts)

print("# ---------- Завдання 4.3 (складніше) ----------")
# Створіть список temperatures із 10 температур. За допомогою list
# comprehension побудуйте список hot_days лише зі значень, більших за
# 30. Одразу після цього спробуйте вивести змінну, яку ви використали
# всередині comprehension (наприклад, print(t), якщо писали
# [t for t in temperatures if t > 30]), і подивіться на помилку. потім перепишіть код так, щоб окремо
# зберегти останню зі значень, більших за 30, у власну змінну, не
# покладаючись на "витік" змінної з comprehension.

"""
for print(t) no errors
"""
temperatures = [10. -34, 23, 88, 92]
DAY_IS_HOT_CONDITION = 30
hot_days = [
    t for t in temperatures
    if t > DAY_IS_HOT_CONDITION
]
last_hot_day = hot_days[-1]

print(hot_days, last_hot_day)
