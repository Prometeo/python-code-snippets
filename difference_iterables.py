def distinct(a, b):
    """ This method finds the difference between two iterables by keeping 
        only the values that are in the first one."""
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


if __name__ == '__main__':
    print(distinct([1, 2, 3], [1, 2, 4]))
