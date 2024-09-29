# tuple is immutable after creation
my_string = "hello"

try:
    print("Trying to change string...")
    my_string[0] = "H"
    
except TypeError as e:
        print("Caught an exception:", e)
    
print("Final string:", my_string)
