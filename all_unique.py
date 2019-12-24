def all_unique(lst):
    """ Checks if the given list has duplicated items or not """
    return len(lst) == len(set(lst))


if __name__ == '__main__':
    x = [1, 2, 2, 3, 4, 5, 6, 7, 8]
    result = all_unique(x)
    print(result)
