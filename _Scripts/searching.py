import random
import time


# # with open("rngNumbers.txt", 'w') as rngNumbers_txt:  # opens and adds random values to a text file
# #     i = 0
# #     while i < seed_value:
# #         rngNumbers_txt.write(str(random.randint(0, 5)) + "\n")
# #         i += 1
#
# with open("rngNumbers.txt", 'r') as rngNumbers_txt:  # opens and adds random values to a text file
#     lyst = [x.strip().split() for x in rngNumbers_txt.readlines()]


result = None


def linear_search(lyst, target):
    lyst_length = len(lyst)
    i = 0

    while i < lyst_length:
        if lyst[i] == target:
            return True
        i += 1

    return False


def binary_search(lyst, target):
    global result
    next_lyst = None
    i = len(lyst) // 2

    if lyst[i] == target:
        result = True

    else:
        if lyst[i] <= target:
            next_lyst = lyst[i:]
            binary_search(next_lyst, target)
        elif lyst[i] >= target:
            next_lyst = lyst[:i + 1]
            binary_search(next_lyst, target)
        else:
            result = False


def jump_search(lyst, target):
    pass


seed_value = 1_000_000
test_lyst = []

for i in range(seed_value):
    random_value = random.randint(0, 5_000)
    test_lyst.append(random_value)

test_lyst.sort()


test_num = 4


def main():
    global result

    start = time.perf_counter()
    result = linear_search(test_lyst, test_num)
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    start = time.perf_counter()
    binary_search(test_lyst, test_num)
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)


if __name__ == "__main__":
    main()
