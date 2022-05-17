# pylint: disable=missing-module-docstring


class SamplePylint:  # pylint: disable=missing-class-docstring, too-few-public-methods
    def __init__(self, number):
        self._number = number

    @classmethod
    def divide(cls, number):  # pylint: disable=missing-function-docstring
        if number == 0:
            raise ZeroDivisionError()


class Children(SamplePylint):  # pylint: disable=missing-class-docstring

    def __init__(self, name, number):
        super().__init__(number)
        self._name = name

    @classmethod
    def some_method(cls, param):  # pylint: disable=missing-function-docstring
        # if param in (1, 2, 3):
        #     return True
        # return False
        return param in (1, 2, 3)

    @classmethod
    def some_method2(cls):  # pylint: disable=missing-function-docstring
        print('bad implementation')


if __name__ == '__main__':
    sample = SamplePylint(10)
    try:
        sample.divide(0)
    except ZeroDivisionError:
        pass
    sample.divide(10)

    # obj = Children('Patryk', 11)
    # obj.some_method(4)
    Children.some_method(4)
