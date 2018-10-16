class Person:

    number = 0;

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def sayHi(self, age):

        print("Hello my name is ", self.name)

        def sayBi(gender):

            age = 12

            print gender.format("{:d} year old {:s}", age, gender)

        return sayBi()

    @classmethod
    def how_many(cls):
        Person.number += 1




person = Person('Isaac', 20)

message = person.sayHi(12)

message('Male')