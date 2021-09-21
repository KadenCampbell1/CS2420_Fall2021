from random import seed, sample
import time


def quicksort(lyst):
    pass


def mergesort(lyst):
    pass


def selection_sort(lyst):
    result = []

    while len(lyst) > 0:
        min_num = lyst[0]

        for i in range(len(lyst)):
            if lyst[i] <= min_num:
                min_num = lyst[i]
                num_index = i

        result.append(lyst.pop(num_index))

    return result


def insertion_sort(lyst):
    result = []
    while len(lyst) > 0:
        num = lyst[0]
        if len(result) is 0:
            result.append(lyst.pop(0))
        for i in range(len(lyst)):
            if result[i] < num:
                result.insert(i-1, lyst.pop(0))


def is_sorted(lyst):
    unsorted_lyst = lyst.copy()
    lyst.sort()
    for i in range(len(lyst)):
        if lyst[i] is not unsorted_lyst[i]:
            return False
    return True


def make_data():
    data_size = 10
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    while True:
        yield data


def main():
    data = make_data()
    lyst = next(data)
    test_lyst = lyst.copy()

    print("-- Selection Sort --")
    start = time.perf_counter()
    result = selection_sort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)
    print(result)

    test_lyst = lyst.copy()

    # timsort


if __name__ == "__main__":
    main()
