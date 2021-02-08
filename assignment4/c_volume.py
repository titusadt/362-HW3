import math


def volume(unit):
   if (unit <= 0):
      raise ValueError("Integer cannot be negative")
   #if not unit.isdigit():
      #raise TyperError("The unit must be an integer")
   return unit*unit*unit
   
