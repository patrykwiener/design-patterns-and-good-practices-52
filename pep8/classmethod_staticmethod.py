class Person:
    HELLO = 'HELLO!'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f'{self.first_name} {self.last_name}')

    @staticmethod
    def say_hello_staticmethod():
        print('Hello!')

    @classmethod
    def say_hello_classmethod(cls):
        print(cls.HELLO)


def say_hello():
    print('Hello!')


if __name__ == '__main__':
    person = Person('Patryk', 'Wiener')
    person.introduce()

    Person.say_hello_staticmethod()
    person.say_hello_staticmethod()

    Person.say_hello_classmethod()
    person.say_hello_classmethod()

    say_hello()
