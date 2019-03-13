def fizzbuzz(up_to: int):
    output = []
    for number in range(1, up_to + 1):
        representation = []

        if number % 3 == 0:
            representation.append('fizz')

        if number % 5 == 0:
            representation.append('buzz')

        if not representation:
            representation.append(str(number))

        output.append(' '.join(representation))

    print(', '.join(output))


if __name__ == '__main__':
    fizzbuzz(100)