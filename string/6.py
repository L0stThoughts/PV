try:
    my_string = "hello" + ["banana", "Strawberry"] # String can't contain lists, sets, or dictionaries
except TypeError as e:
    print("Caught an exception:", e)
