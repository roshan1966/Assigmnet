a = input("Please Enter a String: ")
b = input("Please Enter Number of Repetation of a string: ")
c = int(b)
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string(a, c))
