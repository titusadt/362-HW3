import math

#this code would be run with: python3 no_error_handling.py 

#first get the input from the user

prompt = int(input("Enter a year:"))

if prompt % 4 == 0 and prompt % 100 != 0:
   print(prompt, "is a leap year")
elif prompt % 400 == 0:
   print(prompt, "is a Leap Year")
elif prompt % 100 == 0:
   print(prompt, "is not a Leap Year")
else:
   print(prompt, "is not a Leap Year")
