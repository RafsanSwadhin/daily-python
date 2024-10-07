# Let's enhance your code by adding a **constructor** (`__init__` method). A constructor in Python is a special method used to initialize the attributes of an object when it is created.

# Here's how your code would look with a constructor:

### Code with Constructor


class Student:
    # Constructor method
    def __init__(self, roll, gpa):
        # Initialize the attributes
        self.roll = roll
        self.gpa = gpa

    # Method to display the details
    def display(self):
        print(f"Roll: {self.roll} & GPA: {self.gpa}")

# Creating an object using the constructor
s1 = Student(101, 4.5)

# Display the student's details
s1.display()


### Explanation:
# 1. **Constructor (`__init__`)**: 
#    - The `__init__` method is a special method in Python, called when a new object of the class is created.
#    - It automatically assigns values to the `roll` and `gpa` attributes when the object is instantiated.

# 2. **Parameters in the Constructor**: 
#    - The parameters `roll` and `gpa` are passed when creating an object of the class (`s1 = Student(101, 4.5)`), and they are assigned to the object's attributes (`self.roll` and `self.gpa`).

# 3. **Object Creation**: 
#    - Unlike the previous version where we manually set the details using a separate method, here we directly pass the values to the constructor at the time of object creation.

# 4. **Displaying the Data**: 
#    - The `display()` method is used to print the roll number and GPA of the student.

### Key Benefits of Using a Constructor:
# - **Automatic Initialization**: You don't have to call a separate method to set the details. The constructor initializes the object's attributes as soon as it's created.
# - **Cleaner Code**: It reduces the number of steps and methods you need to call for setting values. This results in more readable and efficient code.

### Output:

# Roll: 101 & GPA: 4.5
