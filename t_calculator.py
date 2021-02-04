import math


print("Enter two numbers")
num_1 = int(input("First Number: "))
num_2 = int(input("Second Number: "))

s1 = "Addition: "
s2 = "Subtraction: "
s3 = "Multipliction: "
s4 = "Division: "

def add(num_1, num_2):
    result_1 = num_1+num_2
    print(s1 + str(result_1))
add(num_1, num_2)

def subtract(num_1, num_2):
    result_2 = num_1-num_2
    print(s2 + str(result_2))
subtract(num_1, num_2)

def multiply(num_1, num_2):
    result_3 = num_1*num_2
    print(s3 + str(result_3))
multiply(num_1, num_2)

def divide(num_1, num_2):
    result_4 = num_1/num_2
    print(s4 + str(result_4))
divide(num_1, num_2)