def get_cleaned_words(text):
    cleaned_words = []
    for word in text.split():
        cleaned_word = word.strip(".,!?;:")
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    return cleaned_words

def word_count(text):
    return len(get_cleaned_words(text))

def longest_word(text):
    cleaned_words = get_cleaned_words(text)

    best_word = ""
    best_length = 0

    for word in cleaned_words:
        len_w = len(word) 
        if len_w > best_length:
            best_word = word
            best_length = len_w

    return best_word


if __name__ == "__main__":
    print("text_tools self-test")

    print(word_count("Hello, world! Hello Python."))   # 4
    print(word_count("...!!!"))                        # 0
    print(word_count(""))                              # 0
    print(longest_word("a bb ccc dd"))                 # ccc
    print(longest_word("Hi, There!"))                  # There
    print(repr(longest_word("")))                      # ''
