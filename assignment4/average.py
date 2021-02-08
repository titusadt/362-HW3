import math


  
def ave(num):
   if(len(num)==0):
      raise ValueError("List is empty")
   elif(sum(num)/ len(num)==0):
      assert (0)
   avg = sum(num)/len(num)
   return avg
