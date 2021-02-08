

def concatenate(f_name, l_name):
   #Check to see if there is an integer in the name
   for x in f_name:
      if (f_name.isdigit()):
         raise TypeError ("First name cannot be an integer")
   for c in l_name:
      if (l_name.isdigit()):
         raise TypeError ("Last name cannot be an integer")
   #make sure that the name array is not empty
   if(len(f_name) == 0):
      raise ValueError(" The first name cant be empty")
   if(len(l_name) == 0):
      raise ValueError(" The last name cant be empty")
   
   return f_name + " " + l_name
