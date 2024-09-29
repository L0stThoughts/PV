# tuple is immutable after creation

my_tuple = (1, 2, 3)

try:
    print("Trying to change tuple...")
    my_tuple[0] = 10
    print("Trying to add an element to tuple...")
    my_tuple += (4,)
except TypeError as e:
        print("Caught an exception:", e)
        
print("Final tuple:", my_tuple)