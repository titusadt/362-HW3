import math

def find(num):
   count = 0
   num1 = 0
   num2 = 1

   if(num == 0):
      return 0

   elif(num == 1):
      return 1

   else:
      while(count < num):
         temp = num1 + num2
         num1 = num2
         num2 = temp
         count += 1
      return num1

def factorial(numb):
   fact = 1;

   for i in range(1, numb + 1):
      fact = fact * i
   return fact
   
