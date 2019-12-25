def get_vowels(var):
    """ This method gets the vowels found in a string """

    return [each for each in var if each in 'aeiou']


if __name__ == '__main__':
    print(get_vowels('foobar'))
    print(get_vowels('gym'))
