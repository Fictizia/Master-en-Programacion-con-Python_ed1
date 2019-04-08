import time


# Solution with lists => for: O(n) * x in list: O(n) = O(n**2)
def repeated(numbers: list) -> list:
    num_visited = []
    num_repeated = []

    for number in numbers:
        if number not in num_visited:
            num_visited += [number]
        elif number not in num_repeated:
            num_repeated += [number]

    return num_repeated


# Solution with sets =>
#   Average case: for: O(n) * x in set: O(1) = O(n)
#   Worst case: for: O(n) * x in set: O(n) = O(n**2)
def repeated_optimized(numbers: list) -> list:
    num_visited = set()
    num_repeated = set()

    for number in numbers:
        if number in num_visited:
            num_repeated.add(number)
        else:
            num_visited.add(number)

    return list(num_repeated)


if __name__ == '__main__':
    start = time.time()
    print('Repeated numbers:', repeated([1, 2, 3, 2, 1, 1]))
    end = time.time()
    print('Execution time:', end - start)

    start = time.time()
    print('Repeated numbers:', repeated_optimized([1, 2, 3, 2, 1, 1]))
    end = time.time()
    print('Execution time:', end - start)