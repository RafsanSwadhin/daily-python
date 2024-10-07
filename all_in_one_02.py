### Instance Variables and Class Variables are two different types of variables in Python classes. Understanding their differences is essential for mastering object-oriented programming (OOP) in Python.

### 1. **Instance Variables**:
# - Instance variables are specific to each object (instance) of a class.
# - These variables are defined inside the methods of a class, typically within the constructor (`__init__`), and are prefixed with `self`.
# - Each object has its own copy of instance variables, meaning changes made to the instance variable in one object do not affect others.

### 2. **Class Variables**:
# - Class variables are shared among all instances of a class.
# - They are defined directly in the class (outside of any method) and are accessed using the class name or through an instance.
# - Changes to the class variable reflect in all instances of the class.



### Example: Instance Variables vs. Class Variables

# Let's see an example to understand the differences.


class Student:
    # Class variable
    school_name = "ABC High School"

    # Constructor to initialize instance variables
    def __init__(self, name, roll):
        # Instance variables
        self.name = name
        self.roll = roll

# Creating two objects (instances) of the Student class
student1 = Student("Rafsan", 101)
student2 = Student("Tasnim", 102)

# Accessing instance variables
print(student1.name)  # Output: Rafsan
print(student2.name)  # Output: Tasnim

# Accessing class variable
print(student1.school_name)  # Output: ABC High School
print(student2.school_name)  # Output: ABC High School

# Changing instance variables
student1.name = "Rafsanul"
print(student1.name)  # Output: Rafsanul
print(student2.name)  # Output: Tasnim  (Unchanged)

# Changing class variable using the class name
Student.school_name = "XYZ High School"
print(student1.school_name)  # Output: XYZ High School
print(student2.school_name)  # Output: XYZ High School

### Explanation:
# - **Class Variable (`school_name`)**:
#   - Defined at the class level and shared among all objects of the class.
#   - When you modify the class variable (`Student.school_name = "XYZ High School"`), it affects all instances of the class, meaning `student1` and `student2` will both reflect the new school name.

# - **Instance Variables (`name`, `roll`)**:
#   - Defined inside the `__init__` constructor and are unique to each object.
#   - When you change the instance variable `name` of `student1`, it doesn’t affect the `name` of `student2`. Both objects maintain their own separate data.

### Key Differences Between Instance and Class Variables:

# | Instance Variable                      | Class Variable                              |
# |----------------------------------------|--------------------------------------------|
# | Belongs to the object (instance).      | Belongs to the class.                      |
# | Defined inside the constructor or methods. | Defined directly in the class body.       |
# | Unique to each object; separate copy for each instance. | Shared across all instances of the class. |
# | Changes in one instance do not affect other instances. | Changes affect all instances.             |
# | Accessed using `self.variable_name`.    | Accessed using `ClassName.variable_name` or `self.variable_name`. |

### Practical Use Cases:

# - **Instance Variables**: Used when you want to store data that is unique to each object. For example, each student has their own name and roll number.
  
# - **Class Variables**: Used when you want to store data that is common to all instances of a class. For example, all students belong to the same school.

# Let me know if you'd like further clarification or additional examples!