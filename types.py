from typing import Callable, List


class Employee:
    def __abs__(self):
        return 1


class Manager(Employee):
    def __len__(self):
        return 10


def salaries(staff: List[Manager],
             accountant: Callable[[Manager], int]) -> List[int]: ...


def se(e: Employee) -> int:
    return abs(e)


def sm(m: Manager) -> int:
    return len(m)


salaries([Manager(), Manager()], sm)


