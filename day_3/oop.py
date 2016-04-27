from person import Person
from kenyan import Kenyan

# ASIDE:
# Read about:
# PEP8
# Instance vs class variables vs.
# class methods (advanced topic) 

# end of class

p = Person('Joe', 23)

print p

p2 = Person('Jane', 23)
p3 = Person('George', 40)

print p.say_hello()

a = [('Jane', 23), ('Joe', 50), 
        ('Jackie', 34), ('Jacob', 23), 
        ('Jee', 18), ('Josh', 60)]

b = []

for name, age in a:
    person = Person(name, age)
    b.append(person)


print Person.people_count
print p2.people_count

k = Kenyan('Miguna', 23)

k.probe(True)
print "Is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()


print p.corrupt
print k.corrupt




