def _is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def fizzbuzz(up_to: int):
    output = []
    for number in range(1, up_to + 1):
        representation_tokens = []

        if _is_divisible(number, 3):
            representation_tokens.append('fizz')

        if _is_divisible(number, 5):
            representation_tokens.append('buzz')

        if not representation_tokens:
            representation_tokens.append(str(number))

        output.append(' '.join(representation_tokens))

    print(', '.join(output))


if __name__ == '__main__':
    fizzbuzz(100)