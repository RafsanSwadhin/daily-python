class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

# Create a Person with default values
person2 = Person()
print(person2.name)  # Output: Unknown
print(person2.age)   # Output: 0