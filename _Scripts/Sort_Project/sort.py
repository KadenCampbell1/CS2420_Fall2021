from random import seed, sample
import time


def quicksort(lyst):
    result = []
    return result


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
        i = 0

        while num == lyst[0]:
            if i == len(result):
                result.append(lyst.pop(0))
            if result[i] > num:
                result.insert(i, lyst.pop(0))
            if len(lyst) == 0:
                return result
            i += 1


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
    print("-- Quick Sort --")
    start = time.perf_counter()
    result = quicksort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)
    print(result)

    # test_lyst = lyst.copy()
    # print("-- Merge Sort --")
    # start = time.perf_counter()
    # result = mergesort(test_lyst)
    # end = time.perf_counter()
    # run_time = end - start
    # sort_result = is_sorted(result)
    #
    # print(run_time)
    # print(sort_result)
    # print(result)

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
    print("-- Insertion Sort --")
    start = time.perf_counter()
    result = insertion_sort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)
    print(result)

    # timsort


if __name__ == "__main__":
    main()
