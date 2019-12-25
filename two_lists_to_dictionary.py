def to_dictionary(keys, values):
    """ This method can be used to convert two lists into a dictionary"""
    return dict(zip(keys, values))


if __name__ == '__main__':
    keys = ["a", "b", "c"]
    values = [2, 3, 4]
    print(to_dictionary(keys, values))
