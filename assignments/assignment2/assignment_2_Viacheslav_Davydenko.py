import random

MAX_TRIES = 6

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

while tries!=0:
    guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
    
    if len(guess)!=wl:
        print("Wrong length. Expected", wl)
        continue

    if guess==w:
        print("You win!!!")
        break

    result=[]; i=0
    while i<wl:
        ch = guess[i]
        if ch==w[i]:
            result.append('correct')
        elif ch in w:
            result.append('present')
        else:
            result.append('absent')
        i+=1

    display=[]
    j=0
    while j<wl:
        s = guess[j]
        res = result[j]
        if res=='correct':
            display.append("["+s.upper()+"]")
        elif res=='present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1

    junk = ''.join([c for c in display if c])
    print("Result:", ' '.join(display))
    tries = tries - 1
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
