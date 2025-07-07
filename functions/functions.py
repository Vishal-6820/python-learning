# why python functions?
# Functions are reusable blocks of code that perform a specific task.
# They help in organizing code, reducing redundancy, and improving readability.

# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible

# print("Welcome to the python leaning platform")



# function create
def welcome()->str:
    """    
    Description : This function will show welcome message.
    
    Return : This function will return the welcome message.
    """
    return " Welcome to the python learning platform"


print(welcome())
print(welcome())
print(welcome())

# parameterized function
def welcome_user(name:str)->str:
    """
    Description : This function will show welcome message with user name.
    
    Parameter : name (str) : Name of the user.
    
    Return : This function will return the welcome message with user name.
    """
    return f"Welcome {name} to the python learning platform... Enjoy your learning journey!" 

print(welcome_user("Vishal"))

# function to add odd and even numbers
def odd_even_sum(lst)->int:
    """
    Description : This function will add odd and even numbers.
    
    Parameter : odd (int) : Odd number.
                even (int) : Even number.
    
    Return : This function will return the sum of odd and even numbers.
    """
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum,odd_sum


# function call
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum = odd_even_sum(numbers)

print(f"Even sum: {even_sum}, Odd sum: {odd_sum}")