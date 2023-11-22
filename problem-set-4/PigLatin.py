def start():
    phrase = input("Phrase: ")
    new_words = []

    words = phrase.split(" ")
    for word in words:
        reconstructed_word = word[1:len(word)]

        first_letter = word[0]
        reconstructed_word += first_letter

        new_words.append(reconstructed_word)

    pig_latin = " ".join(new_words)
    print(pig_latin)


if __name__ == "__main__":
    start()
