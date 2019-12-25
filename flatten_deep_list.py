def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs]if isinstance(
        xs, list) else flat_list.append(xs)
    return flat_list


if __name__ == '__main__':
    print(spread([1, [2], [[3], 4], 5]))
    print(deep_flatten([1, [2], [[3], 4], 5]))
