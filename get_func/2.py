### Example 2: Avoiding KeyError

data = {'a': 10, 'b': 20}

# Using get avoids KeyError
value = data.get('c',0)  # Default to 0 if 'c' is not found
print(value)  # Output: 0
print(data.get('c')) # none
print(data['c'])
# Accessing directly would raise a KeyError
# print(data['c'])  # This would raise a KeyError: 'c'
