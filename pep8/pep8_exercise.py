STRING_CONSTANT = 'Ala ma kota'


def count_message_letters(message):
    counter = 0
    for _ in message:
        counter += 1
    return counter


def modify_message_to_list(message):
    return [
        letter + ' ---------------------------------------------------------------- ' + message
        for letter in message
    ]


class SampleClass:
    some_const = 0
    # SOME_CONST = 0

    def __init__(self):
        self.list = []

    def sample_method(self, item):
        return self.list.append(item)
