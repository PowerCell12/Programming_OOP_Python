def squares(number: int):

    starting = 1

    while starting <= number:

        yield starting  ** 2

        starting += 1

