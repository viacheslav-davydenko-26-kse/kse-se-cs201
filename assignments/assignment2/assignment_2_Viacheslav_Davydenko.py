import random

MAX_TRIES = 6

def clear_word(word):
    return word.strip().lower()

def is_word_valid(word, expected_len):
    if not word.isalpha():
        return False, "The word must contain only letters."
    if len(word) != expected_len:
        return False, f"Wrong length. Expected: {expected_len}"
    return True, "Everything is fine"

def ask_for_guess(tries, expected_word_len):
    guess = input(f"Attempt {tries}/6 – Enter guess: ")

    guess = clear_word(guess)
    
    is_valid, message = is_word_valid(guess, expected_word_len)

    if not is_valid:
        print(message)
        return None 
    else:
        return guess

"""
This function returns string with chars: [c, p, a]
that correspond for status of each char is word in specific position
c - correct
p - present
a - absent
"""
def process_guess(guess, secret_word):
    result = [] 

    for ch_g, ch_s in zip(guess, secret_word):
        if ch_g == ch_s:
            result.append('c')
        elif ch_g in secret_word:
            result.append('p')
        else:
            result.append('a')

    return "".join(result)

words = [
    'apple',
    'bread',
    'candy',
    'dream',
    'eagle',
    'flame',
    'grape',
    'house',
    'input',
    'joker'
]
secret_word = random.choice(words)
secret_word_len = len(secret_word)

print("Welcome to Wordle!")
print(f"Guess the {secret_word_len}-letter word.",
      f"You have {MAX_TRIES} tries.")

tries = 1
while tries <= MAX_TRIES:
    guess = ask_for_guess(tries, secret_word_len)

    if not guess:
        continue

    if guess == secret_word:
        print("You win!!!")
        break

    process_result = process_guess(guess, secret_word)

    display = []
    j = 0
    while j < secret_word_len:
        s = guess[j]
        res = result[j]
        if res == 'correct':
            display.append("["+s.upper()+"]")
        elif res == 'present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1

    junk = ''.join([c for c in display if c])
    print("Result:", ' '.join(display))
    tries += 1
else:
    final = secret_word
    print("You lose! The word was:", final)


"""
====================================================================
REFLECTION
====================================================================

Напишіть тут коротку рефлексію після завершення роботи.

1. Що саме ви змінили?


2. Чому нова структура коду краща?


3. Що ще можна було б додати, змінити або покращити?


"""
