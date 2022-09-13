from ast import walk


class Animal:
    def walk(self):
        print('walk')

class Dog(Animal):
    def bark(self):
        print('bark')

class Cat(Animal):
    def miaw(self):
        print('MIAW')

cat=Cat()
cat.walk()
cat.miaw()
dog=Dog()
dog.walk()
dog.bark()