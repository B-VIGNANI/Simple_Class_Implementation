class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
person1 = Person(input("name: "),input("Age: "))
person2 = Person(input("name: "),input("Age: "))
person1.display_details()
person2.display_details()
