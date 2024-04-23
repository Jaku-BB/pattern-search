from time import time


def naive_pattern_search(pattern, text):
    last_possible_index = len(text) - len(pattern)
    matches = []

    for index in range(last_possible_index + 1):
        if text[index:index + len(pattern)] == pattern:
            matches.append(index)

    return matches


def get_longest_prefix_suffix(pattern):
    longest_prefix_suffix = [0] * len(pattern)
    length = 0

    for index in range(1, len(pattern)):
        while length > 0 and pattern[length] != pattern[index]:
            length = longest_prefix_suffix[length - 1]

        if pattern[length] == pattern[index]:
            length += 1

        longest_prefix_suffix[index] = length

    return longest_prefix_suffix


def knuth_morris_pratt(pattern, text):
    text_length, pattern_length = len(text), len(pattern)

    if pattern_length > text_length:
        return []

    longest_prefix_suffix = get_longest_prefix_suffix(pattern)
    pattern_index = 0
    matches = []

    for index in range(1, text_length):
        while pattern_index > 0 and pattern[pattern_index] != text[index]:
            pattern_index = longest_prefix_suffix[pattern_index - 1]

        if pattern[pattern_index] == text[index]:
            pattern_index += 1

        if pattern_index == pattern_length:
            matches.append(index - pattern_length + 1)
            pattern_index = longest_prefix_suffix[pattern_index - 1]

    return matches


def main():
    file = open('text.txt')

    text = file.read()
    pattern = 'ar'

    file.close()

    start = time()
    result = naive_pattern_search(pattern, text)
    end = time()

    print(f'Naive pattern search: {result}')
    print(f'Naive pattern search time: {end - start}')

    start = time()
    result = knuth_morris_pratt(pattern, text)
    end = time()

    print(f'Knuth-Morris-Pratt: {result}')
    print(f'Knuth-Morris-Pratt time: {end - start}')


if __name__ == '__main__':
    main()
