

def data_type(x):
    '''
    Takes in an argument, x:
        - For a integer, return x ** 2
        - For a float, return x / 2
        - For a string, returns "Hello " + x
        - For a boolean, return "boolean"
        - For a long, return "long"
    '''
    if type(x) == int:
        return x ** 2
    elif type(x) == float:
        return x / 2
    elif type(x) == str:
        return "Hello {}".format(x)
    elif type(x) == bool:
        return "boolean"
    elif type







