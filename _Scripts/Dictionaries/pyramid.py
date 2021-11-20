"""
Project 6: Hashing and Caching
Author: Kaden Campbell
Course: CS2420
Date: 11/11/2021
"""

import sys
from time import perf_counter
from hashmap import HashMap

cache = HashMap()
# cache.set((0, 0), 0)
cache_hit = 0
function_calls = 0


def weight_on(r, c):
    """returns the weight on the item in row r and column c

    arguments:
    r -- type int
    c -- type int
    """

    value = None
    global function_calls
    function_calls += 1
    try:
        cache.get((r, c))
        global cache_hit
        cache_hit += 1
        return cache.get((r, c))
    except KeyError:
        if r == 0 and c == 0:
            cache.set((r, c), 0)
            return 0
        if c == 0:
            value = float((weight_on(r - 1, c) + 200) / 2)
            cache.set((r, c), value)
        if c == r:
            value = float((weight_on(r - 1, c - 1) + 200) / 2)
            cache.set((r, c), value)
        if c != 0 and c != r:
            value = float(((weight_on(r - 1, c) + 200) / 2) + ((weight_on(r - 1, c - 1) + 200) / 2))
            cache.set((r, c), value)
    return value


def main():
    value = sys.argv[1]  # pyramid.py <number> "this is how to use sys.argv[1] in cmd"
    with open("part3.txt", "w") as OUT_FILE:
        start = perf_counter()
        for i in range(int(value)):
            for x in range(0, i + 1):
                OUT_FILE.write(f"{weight_on(i, x):0.2f} ")
            OUT_FILE.write("\n")

        end = perf_counter()
        time = end - start
        OUT_FILE.write(f"\nElapsed time: {time} seconds\n"
                       f"Number of function calls: {function_calls}\n"
                       f"Number of cache calls: {cache_hit}")


if __name__ == "__main__":
    main()

# previous setup
"""
Project 6: Hashing and Caching
Author: Kaden Campbell
Course: CS2420
Date: 11/11/2021


import sys
from time import perf_counter
from hashmap import HashMap

cache = {(0, 0): 0}
cache_hit = 0
function_calls = 0


def weight_on(r, c):
    returns the weight on the item in row r and column c

    arguments:
    r -- type int
    c -- type int
    

    value = None
    global function_calls
    function_calls += 1
    if (r, c) in cache:
        global cache_hit
        cache_hit += 1
        return cache[(r, c)]
    else:
        if r == 0 and c == 0:
            cache[(r, c)] = 0
            return 0
        if c == 0:
            value = float((weight_on(r - 1, c) + 200) / 2)
            cache[(r, c)] = value
        if c == r:
            value = float((weight_on(r - 1, c - 1) + 200) / 2)
            cache[(r, c)] = value
        if c != 0 and c != r:
            value = float(((weight_on(r - 1, c) + 200) / 2) + ((weight_on(r - 1, c - 1) + 200) / 2))
            cache[(r, c)] = value
        cache[(r, c)] = value
    return value


def main():
    cache.clear()
    value = 7  # sys.argv[1]  # pyramid.py <number> "this is how to use sys.argv[1] in cmd"
    # with open("part3.txt", "w") as OUT_FILE:
    #     start = perf_counter()
    #     for i in range(int(value)):
    #         for x in range(0, i + 1):
    #             OUT_FILE.write(f"{weight_on(i, x):0.2f} ")
    #         OUT_FILE.write("\n")
    #
    #     end = perf_counter()
    #     time = end - start
    #     OUT_FILE.write(f"\nElapsed time: {time} seconds\n"
    #                    f"Number of function calls: {function_calls}\n"
    #                    f"Number of cache calls: {cache_hit}")

    cache_temp = HashMap()
    print(cache_temp)


if __name__ == "__main__":
    main()
"""