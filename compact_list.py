def compact(lst):
    """ Removes falsy values (False, None, 0 and "") from a list """
    return list(filter(None, lst))


if __name__ == '__main__':
    result = compact([0, 1, False, 2, '', 3, 'a', 's', 34])
    print(result)
