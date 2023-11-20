def vowel_filter(function):
    def wrapper():

        func  = function()

        list = [i for i in func if i in "aeiouyYAEIOU"]

        return list

    return wrapper
