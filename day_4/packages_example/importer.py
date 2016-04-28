from A.classes import Animal, Poacher, Tourist
from A.functions import word_count, sum_of_digits

# another way
import A.functions as func
import A.classes as classes

print Animal, word_count

print classes.Animal, func.word_count

x = 20
func = x

# {
#     'Animal': <class>,
#     'Poacher': <class>,
#     'Tourist': <class>,
#     'word_count': <func>,
#     'sum_of_digits': <func>,
#     'func':  x,
#     'classes': {
#         'Animal': <class>,
#         'Poacher': <class>
#     },
#     'x': 20
# }
