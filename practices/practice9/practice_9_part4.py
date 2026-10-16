# %% ========== БЛОК 4. САМОСТІЙНЕ НАПИСАННЯ КОДУ (15 хв) ==========

# ---------- Завдання 4.1 (просте) ----------
# Напишіть функцію clean_words(text, min_length=1), яка повертає список слів
# з рядка text:
#   - слова розділяються пробілами (text.split());
#   - з обох кінців кожного слова приберіть розділові знаки ".,!?;:"
#     (word.strip(".,!?;:"));
#   - слова приведіть до нижнього регістру;
#   - у результат потрапляють лише слова, довжина яких >= min_length
#     (порожні рядки після очищення в результат не потрапляють).
# Використайте list comprehension.
def clean_words(text, min_length=1):
    # TODO
    pass


print(clean_words("Hello, world! A test."))         # очікується: ['hello', 'world', 'a', 'test']
print(clean_words("Hello, world! A test.", 2))      # очікується: ['hello', 'world', 'test']
print(clean_words("...!!!"))                        # очікується: []
print(clean_words(""))                              # очікується: []


# %% ---------- Завдання 4.2 (середнє) ----------
# Напишіть дві функції (clean_words із завдання 4.1 використовуйте всередині):
#
# а) word_frequency(*texts) — приймає довільну кількість рядків і повертає
#    словник «слово -> скільки разів воно зустрілось у всіх рядках разом».
#    Слова беріть із clean_words(text). Порядок ключів — за першою появою.
#
# б) most_common(freq) — приймає такий словник і повертає слово з найбільшою
#    кількістю повторень. Якщо таких слів кілька — поверніть те, що йде
#    першим за алфавітом. Для порожнього словника поверніть None.
#
# Обидві функції мають бути чистими: без print() і без змін глобальних
# змінних; вхідний словник у most_common змінювати не можна.
def word_frequency(*texts):
    # TODO
    pass


def most_common(freq):
    # TODO
    pass


freq = word_frequency("a b a", "B c")
print(freq)                                     # очікується: {'a': 2, 'b': 2, 'c': 1}
print(most_common(freq))                        # очікується: a
freq2 = word_frequency("The cat and the dog", "THE end")
print(freq2)                                    # очікується: {'the': 3, 'cat': 1, 'and': 1, 'dog': 1, 'end': 1}
print(most_common(freq2))                       # очікується: the
print(word_frequency())                         # очікується: {}
print(most_common({}))                          # очікується: None
