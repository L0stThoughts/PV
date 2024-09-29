import time

while True:
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(test_list)):
        time.sleep(1)
        print(test_list, end=" ")
        test_list.pop()