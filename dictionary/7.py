import time

while True:
    test_dict = {
        "brand": "Ferrari",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white"]
    }   
    for i in list(test_dict.keys()):
        time.sleep(1)
        print(test_dict, end=" \n")
        del test_dict[i]