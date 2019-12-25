def spread(arg):
    """ This method flattens a list similarly like [].concat(…arr) in JavaScript """
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


if __name__ == '__main__':
    print(spread(([1, 2, 3, [4, 5, 6], [7], 8, 9])))
