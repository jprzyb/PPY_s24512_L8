import random


def choose_word():
    words = ["cat", "dog", "apple", "car", "computer", "book", "television", "programming", "bike",
             "guitar"]
    return random.choice(words)


def main():
    word = choose_word()
    word_length = len(word)

    print(f"Word lenght: {word_length}")
    attempts = 0

    while attempts < 5:
        guess = input(f"Attempt: {attempts+1}/5. Enter character you want to check: ").lower()

        if guess in word:
            print("Yes")
        else:
            print("No")

        attempts += 1

    final_guess = input("Whole word: ").lower()
    if final_guess == word:
        print("You won!")
    else:
        print(f"Game Over! The word was: {word}")


if __name__ == "__main__":
    main()
