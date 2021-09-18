from random import seed, sample
import time
import math


def linear_search(lyst, target):
    lyst_length = len(lyst)
    i = 0

    while i < lyst_length:
        if lyst[i] == target:
            return True
        i += 1

    return False


def binary_search(lyst, target):
    i = len(lyst) - 1
    if i == 0:
        if lyst[i] == target:
            result = True
        else:
            result = False
    elif i == -1:
        result = False
    else:
        if lyst[i] == target:
            result = True
        else:
            i = (len(lyst) // 2)
            if lyst[i] == target:
                result = True
            else:
                if lyst[i] < target:
                    next_lyst = lyst[i + 1:]
                    result = binary_search(next_lyst, target)
                else:
                    next_lyst = lyst[:i]
                    result = binary_search(next_lyst, target)

    return result


def jump_search(lyst, target):
    increment_value = int(math.sqrt(len(lyst)))
    i = increment_value
    while i < len(lyst):
        if lyst[i] >= target:
            if lyst[i] == target:
                return True
            lyst_length = i
            i = lyst_length - increment_value
            while i < lyst_length:
                if lyst[i] == target:
                    return True
                i += 1
            return False
        i = i + increment_value
        if i >= len(lyst) and target > lyst[len(lyst)-1]:
            return False
        if i >= len(lyst):
            i = len(lyst)-1
    return False


def make_data():
    data_size = 10_000_000
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data


def main():
    data = make_data()
    test_lyst = next(data)
    test_num = 1

    print("---linear search for first element.---")

    start = time.perf_counter()
    result = linear_search(test_lyst, test_lyst[0])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---binary search for first element.---")

    start = time.perf_counter()
    result = binary_search(test_lyst, test_lyst[0])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---jump search for first element.---")

    start = time.perf_counter()
    result = jump_search(test_lyst, test_lyst[0])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---linear search for element at the middle.---")

    start = time.perf_counter()
    result = linear_search(test_lyst, test_lyst[len(test_lyst)//2])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---binary search for element at the middle.---")

    start = time.perf_counter()
    result = binary_search(test_lyst, test_lyst[len(test_lyst)//2])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---jump search for element at the middle.---")

    start = time.perf_counter()
    result = jump_search(test_lyst, test_lyst[len(test_lyst)//2])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---linear search for element at the end.---")

    start = time.perf_counter()
    result = linear_search(test_lyst, test_lyst[len(test_lyst)-1])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---binary search for element at the end.---")

    start = time.perf_counter()
    result = binary_search(test_lyst, test_lyst[len(test_lyst)-1])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---jump search for element at the end.---")

    start = time.perf_counter()
    result = jump_search(test_lyst, test_lyst[len(test_lyst)-1])
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---linear search for element NOT in list.---")

    start = time.perf_counter()
    result = linear_search(test_lyst, -1)
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---binary search for element NOT in list.---")

    start = time.perf_counter()
    result = binary_search(test_lyst, -1)
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)

    print("---jump search for element NOT in list.---")

    start = time.perf_counter()
    result = jump_search(test_lyst, -1)
    end = time.perf_counter()
    run_time = end - start

    print(run_time)
    print(result)


if __name__ == "__main__":
    main()
