from functools import wraps


def log_parameters(label):
    def _decorator(target):
        @wraps(target)
        def _decorated(*args, **kwargs):
            print(f"[{label}] Called with {args} and {kwargs}")
            return target(*args, **kwargs)

        return _decorated

    return _decorator


def log_return(label):
    def _decorator(target):
        @wraps(target)
        def _decorated(*args, **kwargs):
            result = target(*args, **kwargs)
            print(f"[{label}] Returned {result}")
            return result

        return _decorated

    return _decorator


def log(label):
    def _decorator(target):
        @log_parameters(label)
        @log_return(label)
        @wraps(target)
        def _decorated(*args, **kwargs):
            return target(*args, **kwargs)

        return _decorated

    return _decorator


@log("XXX")
def solve(a, b, c):
    """Solves a quadratic equation given the coefficients."""
    root = (b ** 2 - 4 * a * c) ** 1 / 2
    return (-b + root) / 2 * a, (-b - root) / 2 * a


solve(4, 2, 1)
solve(16, 25, c=5)
