# Method to chunk a  list into smaller lists of a specified size


def chunk(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result = chunk(lst, 3)
    print(result)
