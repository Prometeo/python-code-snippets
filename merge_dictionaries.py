def merge_two_dicts(a, b):
    """ Thie method can be used to merge two dictionaries """

    c = a.copy()
    c.update(b)
    return c


def merge_two_dicts_simpler(a, b):
    """ With python 3.5 and above """

    return {**a, **b}


if __name__ == '__main__':
    a = {'x': 1, 'y': 2}
    b = {'y': 3, 'z': 4}
    print(merge_two_dicts(a, b))
    print(merge_two_dicts_simpler(a, b))
