from random import seed, sample
import time


def quicksort(lyst):
    low = []
    high = []
    result = []
    while len(lyst) > 1:
        pivot = lyst.pop(0)
        lyst_len = len(lyst)
        i = 0
        while i < lyst_len:
            if pivot > lyst[0]:
                low.append(lyst.pop(0))
            else:
                high.append(lyst.pop(0))
            i += 1
        low.append(pivot)

    for i in low:
        result.append(i)
    for i in high:
        result.append(i)

    if not is_sorted(result):
        result = quicksort(result)

    return result


def mergesort(lyst):
    result = []
    left_half = []
    right_half = []

    def half_lyst(h_lyst, low_high=None):
        lyst_len = len(h_lyst) // 2
        if lyst_len > 0:
            half_lyst(h_lyst[:lyst_len], False)
            half_lyst(h_lyst[lyst_len:], True)
        else:
            if low_high is False:
                left_half.append(h_lyst)
            if low_high is True:
                right_half.append(h_lyst)
        # return h_lyst

    def sort_lyst(s_lyst):
        return_lyst = []
        for i, l in s_lyst:
            print("i: " + i + "\n" + "l: " + l)
        i = 0
        while i < len(s_lyst):
            if len(s_lyst) == 1:
                return_lyst.append(s_lyst.pop(0))
            elif s_lyst[0] < s_lyst[1]:
                return_lyst.append(s_lyst.pop(0))
            else:
                return_lyst.append(s_lyst.pop(1))

        return return_lyst

    half_lyst(lyst)


    i = 0
    while i < len(lyst):
        if lyst[0] < lyst[1]:
            result.append(lyst.pop(0))
        else:
            result.append(lyst.pop(1))
        i += 1

    return result


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

    test_lyst = lyst.copy()
    print("-- Merge Sort --")
    start = time.perf_counter()
    result = mergesort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)
    print(result)

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
