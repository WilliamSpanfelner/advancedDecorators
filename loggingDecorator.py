# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        sum_of_args = function(*args)
        function_name = function.__name__
        # sum_of_args = sum([arg for arg in args])
        return f"You called {function_name}{args} \nIt returned: {sum_of_args}"
    return wrapper

# Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)

print(a_function(1, 2, 3))
