


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ToString(self):
        print("Hello my name is {} and I am {} years old.".format(self.name, self.age))



kendrick = Person('Kendrick', '11')
galen = Person('WaddleGuy', '50')
helper = VowelHelper()
print(helper.x)
print(kendrick.name)
kendrick.ToString()
galen.ToString()
