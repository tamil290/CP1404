# Word Occurrences


def main():
    # call count_words function to get word counts
    word_counts = count_words()

    # sort word counts by word and format output
    max_word_len = max(len(word) for word in word_counts.keys())
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_len}} : {count}")


def count_words():
    # ask user for input string
    text = input("Text: ")

    # count occurrences of words using a dictionary
    word_counts = {}
    for word in text.split():
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts


main()