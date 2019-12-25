def decapitalize(var):
    """ This method can be used to turn the first letter of the given string 
        into lowercase """
    return var[:1].lower() + var[1:]


if __name__ == '__main__':
    print(decapitalize('FooBar'))
