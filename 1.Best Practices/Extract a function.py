def standardize(column):
#   Standardize the values in a column.

#   Args:
#     column (pandas Series): The data to standardize.

#   Returns:
#     pandas Series: the values as z-scores

  # Finish the function so that it returns the z-scores
  z_score = (df - y1_gpa.mean()) / df.y1_gpa.std()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()
