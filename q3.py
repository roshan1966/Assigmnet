varVal1 = int(input("Please Enter Your 1st Number: "))
varVal2 = int(input("Please Enter Your 2nd Number: "))
def my_function():
    a = int(varVal1)
    b = int(varVal2)
    c = varVal1 / varVal2
    d = "It is not completely divisible"
    e = "It is completely divisible"
    if int(c) == 0 or int(c) == 1:
      return e
    else:
      return d
print(my_function())
