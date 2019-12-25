def most_commmon(lst):
    """ This method returns the most frequent element that appears in a list """

    return max(set(lst), key=lst.count)


if __name__ == '__main__':
    numbers = [1, 2, 1, 2, 3, 2, 1, 4, 2]
    print(most_commmon(numbers))
