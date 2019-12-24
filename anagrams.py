from collections import Counter


def anagram(first, second):
    """ This method checks if two strings are anagrams """
    return Counter(first) == Counter(second)


if __name__ == '__main__':
    result = anagram('abcd3', '3acdb')
    print(result)
