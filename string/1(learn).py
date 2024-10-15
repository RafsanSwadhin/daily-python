# **Immutable** means that an object cannot be changed after it is created. In Python, immutable data types are those whose content or state cannot be altered once the object is instantiated.

# For example, strings in Python are immutable:
# ```python
# s = "Rafsan"
# s[0] = "X"  # This will raise an error
# ```
# In this case, you cannot change the first character of the string, because the string itself cannot be modified.

# Key points about immutability:
# - **No in-place modification**: Once created, the object's content is fixed. Any operation that appears to "modify" the object actually creates a new one.
# - **Memory efficiency**: Because immutable objects can't change, they can be stored more efficiently and reused, which can save memory.
# - **Thread safety**: Immutable objects can be shared between threads without needing to worry about one thread modifying the object, which makes them safer in concurrent programming.

# Examples of immutable types in Python:
# - **Strings**: As shown earlier.
# - **Tuples**: A tuple cannot be changed once created.
# - **Numbers**: Integers and floats are immutable.

# Mutable objects (which can be changed) include lists, dictionaries, and sets.