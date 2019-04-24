from functools import partial
from timeit import timeit


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


def log_result(fn, type_list, num_list):
    print("Repeated numbers:", fn(num_list))
    execution_time = timeit(partial(fn, num_list), globals=globals(), number=100)
    print(f"Execution time of {fn.__name__} with {type_list}: {execution_time}")


if __name__ == "__main__":
    # Big O notation describes the limiting behaviour of a function when the argument
    # tends towards a particular value or infinity, so we need a list with more numbers
    # to get a proper value
    small_list = [1, 2, 3, 2, 1, 1]
    big_list = [num for num in range(1, 51)] * 1000

    print("\n=== EXEC WITH SMALL LIST ===")
    log_result(repeated, "small list", small_list)
    log_result(repeated_optimized, "small list", small_list)

    print("\n=== EXEC WITH BIG LIST ===")
    log_result(repeated, "big list", big_list)
    log_result(repeated_optimized, "big list", big_list)

