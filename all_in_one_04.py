# Encapsulation

class BankAccount:
    def __init__(self, balance):
        # Private attribute (balance)
        self.__balance = balance

    # Public method to check balance
    def check_balance(self):
        return f"Your current balance is: {self.__balance}"

    # Public method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is: {self.__balance}")

    # Public method to withdraw money
    def withdraw(self, amount):
        if self.__can_withdraw(amount):  # Calling private method
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is: {self.__balance}")
        else:
            print("Insufficient balance!")

    # Private method to check if withdrawal is possible
    def __can_withdraw(self, amount):
        return self.__balance >= amount

# Create an object of BankAccount with an initial balance of 1000
my_account = BankAccount(1000)

# Check balance
print(my_account.check_balance())  # Output: Your current balance is: 1000

# Deposit money
my_account.deposit(500)  # Output: Deposited 500. New balance is: 1500

# Try to withdraw money
my_account.withdraw(200)  # Output: Withdrew 200. New balance is: 1300

# Try to withdraw more than the balance
my_account.withdraw(2000)  # Output: Insufficient balance!

# Your current balance is: 1000
# Deposited 500. New balance is: 1500
# Withdrew 200. New balance is: 1300
# Insufficient balance!




# Encapsulation in Simple Terms:
# Encapsulation means hiding the internal details of an object and only exposing the necessary parts. You control what information or data can be accessed and modified from outside the class.

# In Python, we achieve encapsulation by making:

# Public members (accessible from anywhere).
# Private members (hidden and only accessible inside the class).
# Example: Simple Bank Account
# Let's imagine a bank account where you can:

# Check your balance (public).
# Deposit money (public).
# Withdraw money, but only if you have enough balance (private method handles this).


#Explanation:
# Private Attribute (__balance):

# The balance of the bank account is private (__balance). This means you cannot access it directly from outside the class. This protects the balance from being modified directly by anyone.
# Public Methods:

# check_balance(), deposit(), and withdraw() are public methods that allow you to interact with the account. You can call these methods from outside the class to view and modify the balance.
# The balance is updated only via these public methods, ensuring controlled access to the balance.
# Private Method (__can_withdraw()):

# The __can_withdraw() method is a private method. It checks if there's enough balance before allowing a withdrawal. Since this logic is hidden (encapsulated), you can’t directly call __can_withdraw() from outside the class.
# Encapsulation in Action:

# You can check balance and deposit money freely.
# When withdrawing money, the class ensures you only withdraw if there’s enough balance. This is an example of encapsulation, where important internal logic (like checking the balance) is hidden, and you only interact with the class in a controlled way.
# Key Points:
# Public members (like check_balance()) are accessible from anywhere.
# Private members (like __balance and __can_withdraw()) are hidden and protected from outside access, keeping the internal workings safe.
# By using encapsulation, we make sure the account's balance can only be updated in a controlled way, preventing direct access or modification that could lead to errors.