import random

list_of_words = ["the", "at",	"there",	"some", "my", "of",	"be",	"use",	"her",	"than", "and",	"this",	"an",	"would",	"first", "a",	"have",	"each",	"make",	"water", "to",	"from",	"which",	"like",	"been", "in",	"or",	"she",	"him",	"call", "is",	"one",	"do",	"into",	"who", "you",	"had",	"how",	"time",	"oil", "that",	"by",	"their",	"has",	"its", "it",	"word",	"if",	"look",
                 "now", "he",	"but",	"will",	"twofind", "was",	"not",	"up",	"more",	"long", "forwhat",	"other",	"write",	"down", "on",	"all",	"about",	"go",	"day", "are",	"were",	 "out",	"see",	"did", "as",	"we",	 "many",	"number",	"get", "with",	"when",	"then",	"no",	"come", "his",	"your",	"them",	"way",	"made", "they",	"can",	"these",	"could",	"may", "I",	"said",	"so",	"people",	"part"]


def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    min = int(input("Enter the minimum number: "))
    max = int(input("Enter the maximum number: "))
    append_random_numbers(numbers, 3, min, max)
    print(numbers)

    words = []
    append_random_words(words)
    print(words)
    append_random_words(words, 3)
    print(words)

    print(numbers, words)


def append_random_numbers(numbers_list, quantity=1, min=1, max=10):
    """
    Appends a pseudo random number to a list.
        Parameters:
        number_list: This list that the pseudo random number is appedned to
        quantity: The number of pseudo random numbers to append
        min: The minimum range that the pseudo random number can be
        max: The maximum range that the pseudo random number can be
    Returns:
        None
    """
    for i in range(quantity):
        random_number = round(random.uniform(min, max), 1)
        numbers_list.append(random_number)


def append_random_words(words_list, quantity=1):
    """
    Appends a pseudo random word to a list.
        Parameters:
        words_list: This list that the pseudo random word is appedned to
        quantity: The number of pseudo random words to append
    Returns:
        None
    """
    for i in range(quantity):
        random_word = random.choice(list_of_words)
        words_list.append(random_word)


if __name__ == '__main__':
    main()
