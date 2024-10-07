class Student:
    def set_details(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa 
    def display(self):
        print(f"Roll:{self.roll} & GPA:{self.gpa}")

s1 = Student()
s1.set_details(101,4.5)
s1.display()

# To teach you about *classes* and *objects* without using constructors, let's first break down these concepts.

# ### Class and Object Overview:
# - *Class*: A blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that the objects created from the class will have.
# - *Object*: An instance of a class. It represents a specific entity created based on the class definition.

# When using a class without a constructor (i.e., without the __init__ method), the object is created directly from the class. Any attributes or methods in the class can be accessed through the object after it’s created.

# ### Example (Without Constructor):
# We'll create a simple class Student with two attributes: roll and gpa. We won't use a constructor (__init__). Instead, we'll assign the values manually after the object is created.

# # Define a class without a constructor
# class Student:
#     # Class definition
#     def set_details(self, roll, gpa):
#         self.roll = roll
#         self.gpa = gpa

#     def display(self):
#         print(f"Roll: {self.roll}, GPA: {self.gpa}")

# # Create an object of the Student class
# student1 = Student()

# # Manually setting attributes using a method
# student1.set_details(101, 3.85)

# # Display the details
# student1.display()

# ### Explanation:
# - **Class Definition (Student)**: It contains two methods, set_details and display.
# - **Method (set_details)**: This method takes roll and gpa as arguments and assigns them to the object using self.
# - *Object Creation*: We create an object student1 from the Student class.
# - *Setting Attributes*: We manually set the attributes roll and gpa by calling the set_details method.
# - *Displaying the Object’s Data*: The display method is used to print the values of roll and gpa.

# ### How it Works Without a Constructor:
# - Normally, the constructor (__init__) is used to initialize attributes when the object is created. However, in this example, we use the set_details method to initialize the attributes after the object is created.

# This approach gives you flexibility when you don’t need to define initial values upon object creation.