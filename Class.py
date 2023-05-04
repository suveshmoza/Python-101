# A class is a blueprint for creating objects that have specific attributes and behaviors.
# A class encapsulates data and functions that operate on that data into a single unit,
# making it easier to manage and reuse code.

# A class is defined using the class keyword, followed by the name of the class and a colon.

# Parent class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} says {self.sound}')

# Child classes inheriting from parent class Animal


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'woof')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'meow')

# Encapsulation example


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0 and age < 120:
            self.__age = age

# Abstraction example


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

# Polymorphism example


def make_sound(animal):
    animal.make_sound()


dog = Dog('Fido')
cat = Cat('Whiskers')
make_sound(dog)
make_sound(cat)

person = Person('John', 30)
print(person.get_age())
person.set_age(40)
print(person.get_age())

square = Square(5)
circle = Circle(3)
print(square.area())
print(circle.area())
