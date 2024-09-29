try: 
    my_set = {"apple", "banana", "cherry", None}
    print("Element at index 0:", my_set[0])
except TypeError as e:
    print("Caught an exception:", e)