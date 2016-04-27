# unpacking
def hello(name, age, class_=''):
    '''
    Explains....
    '''
    if class_ != '':
        return "I am {}, {} y/o, and {} class".format(name, age, class_)
    return "I am {}, and I'm {}".format(name, age)


people = [
            ("Jane", 23, 'High'),
            ("Joe", 25, 'Low'),
            ("Brian", 60),
            ("Betty", 45)
            ]

# for name, age in people:
#     print hello(anme, age)

# use of unpacking

for person in people:
    print hello(*person)









