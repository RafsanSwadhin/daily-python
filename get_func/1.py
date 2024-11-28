### Syntax:

# dictionary.get(key, default_value)

### Example 1: Basic Usage

data = {'name': 'Alice', 'age': 25}

# Retrieve existing key
print(data.get('name'))  # Output: Alice

# Retrieve non-existing key with default value
print(data.get('gender', 'Not Specified'))  # Output: Not Specified
print(data.get('age', 'Not Specified')) # though there is a default value, but output is 25
# Retrieve non-existing key without default value
print(data.get('city'))  # Output: None