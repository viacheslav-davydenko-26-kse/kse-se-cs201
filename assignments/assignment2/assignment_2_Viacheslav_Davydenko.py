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

def make_guess_status_display_string(guess, process_result):
    display = []

    for ch_g, ch_r in zip(guess, process_result):
        status = ""
        if ch_r == 'c':
            status = f"[{ch_g.upper()}]"
        elif ch_r == 'p':
            status = f"({ch_g})"
        else:
            status = f" {ch_g} "
        display.append(status)

    return "".join(display)

def welcome():
    print("Welcome to Wordle!")

def congratulate():
    print("*************")
    print("!!!You win!!!")
    print("*************")

def show_lose_message(secret_word):
    print("You lose! The word was:", secret_word)

def goodbye():
    print("Thanks for the game!")

def ask_for_guess(tries, expected_word_len):
    guess = input(f"Attempt {tries}/6 – Enter guess: ")

    guess = clear_word(guess)
    
    is_valid, message = is_word_valid(guess, expected_word_len)

    if not is_valid:
        print(message)
        return None 
    else:
        return guess

def play(words):
    secret_word = random.choice(words)
    secret_word_len = len(secret_word)

    print(f"Guess the {secret_word_len}-letter word.",
          f"You have {MAX_TRIES} tries.")

    tries = 1
    while tries <= MAX_TRIES:
        guess = ask_for_guess(tries, secret_word_len)
        if not guess:
            continue

        if guess != secret_word:
            process_result = process_guess(guess, secret_word)
            display = make_guess_status_display_string(guess, process_result)

            print("Result:", display)
        else:
            congratulate()
            break

        tries += 1
    else:
        show_lose_message(secret_word)


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

welcome()

try:
    is_playing = True
    while is_playing:
        play(words)
        answer = input("Do you want to play another game? (Y/n): ")
        is_playing = answer.lower() == "y" 
except KeyboardInterrupt:
    print("\nForced end of the game.") 

goodbye()

"""
====================================================================
REFLECTION
====================================================================

Напишіть тут коротку рефлексію після завершення роботи.

1. Що саме ви змінили?


2. Чому нова структура коду краща?


3. Що ще можна було б додати, змінити або покращити?


"""
