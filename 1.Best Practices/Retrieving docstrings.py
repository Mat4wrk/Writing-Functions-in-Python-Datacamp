# Begin by getting the docstring for the function count_letter(). Use an attribute of the count_letter() function.
# Get the docstring with an attribute of count_letter()
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))


# Now use a function from the inspect module to get a better-formatted version of count_letter()'s docstring.
import inspect

# Get the docstring with a function from the inspect module
docstring = (inspect.getdoc(count_letter))

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))


# Use the inspect module again to get the docstring for any function being passed to the build_tooltip() function.
def build_tooltip(function):
  """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
