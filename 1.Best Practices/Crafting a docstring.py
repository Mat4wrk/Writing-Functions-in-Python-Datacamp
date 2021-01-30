# Copy the following string and add it as the docstring for the function: Count the number of times `letter` appears in `content`.
# Add a docstring to count_letter(
def count_letter(content, letter):
# Count the number of times `letter` appears in `content`.
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])
  
  
# Now add the arguments section, using the Google style for docstrings. Use str to indicate a string.
def count_letter(content, letter):
#   Count the number of times `letter` appears in `content`.

#   # Add a Google-style arguments section
#   Args:
#     content (str): The string to search.
#     letter (str): The letter to search for.

  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])
  
  
#   Add a returns section that informs the user the return value is an int.
def count_letter(content, letter):
#   Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  # Add a returns section
  Returns:
    int
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('"letter" must be a single character string.')
  return len([char for char in content if char == letter])


# Finally, add some information about the ValueError that gets raised when the arguments aren't correct.
def count_letter(content, letter):
  # Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])
