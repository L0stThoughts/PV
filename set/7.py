import time

while True:
    test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(len(test_set)):
        time.sleep(1)
        print(test_set, end=" ")
        test_set.pop()