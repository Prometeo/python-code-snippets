def palindrome(a):
    """ This method checks whether a given string is a palindrome """
    return a == a[::-1]


if __name__ == '__main__':
    print(palindrome('mom'))
