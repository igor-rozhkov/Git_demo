class Dog:
    biology_class = 'Animal'
    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color

    def run(self):
        return 'I can run!'

    def get_name(self):
        return f'Hello! My name is {self.__name}'

    def set_name(self, new_name):
        self._name = new_name

# dog1 = Dog('Bobik', 3, 'brown')
# print(dog1.name)
# print(dog1.get_name())
# print(dog1.color)
# print(dog1.run())
# print(dog1.biology_class)
#
dog2 = Dog('Rex', 5, 'black')
print(dog2.biology_class)
print(dog2.get_name())

print(dog2.set_name('Snoopy'))
print(dog2.get_name())
print(dog2.__dict__)


class Pitbull(Dog):
    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    # переопределили метод give_a_paw от родительского класса---
    def give_a_paw(self):
        return 'I can give a paw!'
    def run(self):
        return 'I can run fast then Dog2!'


# dog3 = Pitbull('Lassie', 8, 'black', 'type1')
# print(dog3.get_name())
# print(dog3.biology_class)
# print(dog3.give_a_paw())
# print(dog3.run())
# print(dog2.run())

        #object has no attribute 'give_a_paw'(нет в родительском классе)
#print(dog2.give_a_paw())

