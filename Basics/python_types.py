# Tuple
# A tuple is a collection which is ordered and unchangeable.
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
this_tuple = (1, [1, 2, 3], {'a': 10}, 4.5, "cherry")
print(type(this_tuple))
print(this_tuple)
print(this_tuple[0])
print(this_tuple[1])
print(this_tuple[2])
print(this_tuple[3])
print(this_tuple[4])

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
this_set = {"apple", "banana", "cherry", "cherry"}
print(type(this_set))
print("this_set", this_set)


# this_tuple[0] = 34 xxxxx #Tuple does not support item assignment

# Class.
# In Python, a class is an object of the class type.
class TypeClass:
    def __init__(self):
        self.a = 45
        self.b = [2, 4, 5],
        self.c = {'aa': 'string'}
        self.d = (1, [1, 2, 3], {'a': 10}, 4.5, "cherry")


type_class = TypeClass()
print('class', type_class)
print('type_class attribute of a', type_class.a)

# Dictionary. It is also hash table
type_dict = {'a': 45,
             'b': [2, 4, 5],
             'c': {'aa': 'string'}}
print(type_dict)
print(type(type_dict))

# List
type_list = [3, 5, 6, 7, 'string']
print(type(type_list))
print(type_list)
