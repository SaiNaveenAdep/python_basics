"""
@Clever Programmer

Write a function bigger_guy that takes in
two numbers and returns the bigger one.

MAKE SURE to use RETURN and not PRINT in your function.
*** Important: DO NOT forget to IMPORT this into main.py ***

"""

def bigger_guy(a, b):
  if a >b:
      return a
  else:
      return b

  print(bigger_guy(20,4))
  """
  Given 2 numbers, return the bigger one.
  >>> bigger_guy(2, 3)
  3
  """