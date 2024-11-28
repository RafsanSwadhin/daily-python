print("0%5", 0 % 5)      # 0
print("1%5", 1 % 5)      # 1
print("2%5", 2 % 5)      # 2 a%b=a−b×⌊a/b⌋ here ⌊a/b⌋ we will take the largest integer less than or equal to ⌊a/b⌋
print("2%5", 2 % -5)      
print("3%5", 3 % 5)      # 3
print("4%5", 4 % 5)      # 4
print("5%5", 5 % 5)      # 0
print()
print("-0%5", -0 % 5)    # 0
print("-1%5", -1 % 5)    # 4
print("-2%5", -2 % 5)    # 3
print("-3%5", -3 % 5)    # 2
print("-4%5", -4 % 5)    # 1
print("-5%5", -5 % 5)    # 0
print()
print("-6%5", -6 % 5)    # 4
print("-7%5", -7 % 5)    # 3
print("-8%5", -8 % 5)    # 2
print("6%5", 6 % 5)      # 1
print("7%5", 7 % 5)      # 2
print("8%5", 8 % 5)      # 3
print(0 % 4)             # 0
print(0 % -4)            # 0


# Let's break down how `-a % b` and `a % b` behave in different scenarios depending on the relationship between \( a \) and \( b \). We'll walk through each case with clear examples.

# ---

# ### **Case 1: `a > b`**
# - \( a \) is larger than \( b \).

# #### **1.1: `a % b`**
# The remainder is simply \( a - b \times \lfloor a / b \rfloor \).

# #### **1.2: `-a % b`**
# The result is adjusted to stay in the range \([0, b)\). It can be calculated as:
# \[
# -a \% b = b - (a \% b)
# \]

# #### **Example**:
# Let \( a = 7 \), \( b = 5 \):
# - `a % b`:
#   \[
#   7 \% 5 = 7 - 5 \times \lfloor 7 / 5 \rfloor = 7 - 5 \times 1 = 2
#   \]

# - `-a % b`:
#   \[
#   -7 \% 5 = 5 - (7 \% 5) = 5 - 2 = 3
#   \]

# **Output**:
# ```python
# print(7 % 5)   # 2
# print(-7 % 5)  # 3
# ```

# ---

# ### **Case 2: `a < b`**
# - \( a \) is smaller than \( b \).

# #### **2.1: `a % b`**
# Here, \( a \% b = a \) because \( a \) is less than \( b \), and no full division happens.

# #### **2.2: `-a % b`**
# The result adjusts to be positive, so:
# \[
# -a \% b = b - (-a)
# \]

# #### **Example**:
# Let \( a = 3 \), \( b = 5 \):
# - `a % b`:
#   \[
#   3 \% 5 = 3
#   \]

# - `-a % b`:
#   \[
#   -3 \% 5 = 5 - 3 = 2
#   \]

# **Output**:
# ```python
# print(3 % 5)   # 3
# print(-3 % 5)  # 2
# ```

# ---

# ### **Case 3: `a == b`**
# - \( a \) is equal to \( b \).

# In this case:
# \[
# a \% b = 0
# \]
# \[
# -a \% b = b
# \]

# #### **Example**:
# Let \( a = 5 \), \( b = 5 \):
# - `a % b`:
#   \[
#   5 \% 5 = 0
#   \]

# - `-a % b`:
#   \[
#   -5 \% 5 = 5 - (5 \% 5) = 5 - 0 = 5
#   \]

# **Output**:
# ```python
# print(5 % 5)   # 0
# print(-5 % 5)  # 5
