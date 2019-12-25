def has_duplicates(lst):
    """ The method checks whether a list has duplicate values 
        by using the fact that set() contains only unique elements."""

    return len(lst) != len(set(lst))


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 5]
    y = [1, 2, 3, 4, 5]
    print(f'{x} has duplicates: {has_duplicates(x)}')
    print(f'{y} has duplicates: {has_duplicates(y)}')
