class User:
    def __init__(self, name):
        """
        Take a name to initialise object
        :param name: a string
        """
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    """
    Checks whether a user object's is_logged_in property is set to true
    :param function: A function that has taken a user object as an argument.
    :return: the wrapped function
    """
    # Access the user passed in by giving the wrapper function unlimited args and kwargs.
    # Since the user argument is the first declared in the create_blog_post function, it
    # can be referenced by args[0] instead of user as it would normally be reference within
    # the create_blog_post function.
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    """
    Prints a string to the console including the user's name.
    :param user: a user object
    """
    print(f"This is {user.name}'s new blog post.")


new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)
