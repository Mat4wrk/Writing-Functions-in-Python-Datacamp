# Decorate print_sum() with the add_hello() decorator to replicate the issue that your friend saw - that the docstring disappears.
def add_hello(func):
  def wrapper(*args, **kwargs):
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
# Adds two numbers and prints the sum
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


# To show your friend that they are printing the wrapper() function's docstring, not the print_sum() docstring, add the following docstring to wrapper():
def add_hello(func):
  # Add a docstring to wrapper
  def wrapper(*args, **kwargs):
#     Print 'hello' and then call the decorated function.
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
#   Adds two numbers and prints the sum
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


# Import a function that will allow you to add the metadata from print_sum() to the decorated version of print_sum().
# Import the function you need to fix the problem
from functools import wraps

def add_hello(func):
  def wrapper(*args, **kwargs):
#     Print 'hello' and then call the decorated function.
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
#   Adds two numbers and prints the sum
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


# Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function.
from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
#     Print 'hello' and then call the decorated function.
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
#   Adds two numbers and prints the sum
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)
