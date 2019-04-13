def valid_annotations(target):
    def _decorated(*args, **kwargs):
        print(f"Called with {args} and {kwargs}")
        annotations = target.__annotations__
        list_annotations_var_names = list(target.__annotations__.keys())
        set_annotations_var_names = set(target.__annotations__.keys())
        set_kwargs_var_names = set(kwargs.keys())

        not_kwargs_var_names = set_annotations_var_names.difference(
            set_kwargs_var_names
        )
        all_args_with_keys = kwargs

        for var_name in not_kwargs_var_names:
            var_annotation_index = list_annotations_var_names.index(var_name)
            all_args_with_keys[var_name] = args[var_annotation_index]

        for var_name in set_annotations_var_names:
            if type(all_args_with_keys[var_name]) != annotations[var_name]:
                return "Los tipos de los parámetros no son correctos"

        return target(**all_args_with_keys)

    return _decorated


@valid_annotations
def solve(a: int, b: int, c: int):
    """Solves a quadratic equation given the coefficients."""
    root = (b ** 2 - 4 * a * c) ** 1 / 2
    return (-b + root) / 2 * a, (-b - root) / 2 * a


print(solve(4, 2, 1))
print(solve("a", 2, 1))
print(solve(4, 2, c=1))
