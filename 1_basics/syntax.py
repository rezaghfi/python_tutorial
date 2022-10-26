print("-----------------indentation----------------")
# Python uses indentation to indicate a block of code.
# Python will give you an error if you skip the indentation:
"""
if 5 < 2:
print("5 is bigger than 2")
"""
#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 4 > 2:
  print("4 is bigger than 2")
if 5 > 2:
      print("5 is bigger than 2")
#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
"""
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
print("-----------------python variable----------------")
x = 5
y = "Hello, World!"
print("x=",x,"and y=", y)
print("-----------------comments----------------")
print("comment in single line use # and in multiple line use double \"\"\" ")   #this is a comment
print("-----------------creating variable----------------")
#A variable is created the moment you first assign a value to it.
x = 4
y = "john"
print(x)
print(y)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4 # x is of type int
x = "Sally" # x is now of type str
print("-----------------casting variable----------------")
print(x)
x = str(3)  # x is '3'
y = int(3) #y is 3
z = float(3) #z will be 3.0
print("-----------------get the type----------------")

x = 5
y = "john"
print(type(x))
print(type(y))
print("-----------------single or double quotes----------------")
x = "John"
# is the same as
x = 'John'
print("-----------------case-sensitive----------------")
a = 4
A = "Sally"
# A will not overwrite a
print("-----------------variable Names----------------")
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
ILLIGAL VARIABLE NAMES:
2myvar = "John"
my-var = "John"
my var = "John"
"""
print("-----------------Multi Words Variable Names----------------")
print("CamelCase")
print("PascalCase")
print("snake_case")
print("-----------------Many Values to Multiple Variables----------------")
x , y , z = 1, 3, 4
print(x, y, z)
print("-----------------One Value to Multiple Variables----------------")
x = y = z = "orange "
print(x, y, z)
print("-----------------unpack collection----------------")
fruits = ["apple", "banana", "cherry"]
print(x, y, z)
print("-----------------print function----------------")
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)
#In the print() function, you output multiple variables, separated by a comma:
x , y , z = "Python" , " is " , "awesome"
print(x, y, z)
#You can also use the + operator to output multiple variables:
print(x + y + z)
#For numbers, the + character works as a mathematical operator:
x , y = 2 , 5
print(x + y)
#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""
x = 3
y = "John"
print(x + y)
"""
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 3
y = "John"
print(x, y)
print("-----------------Global Variable----------------")
x = "awesome"
def myfunc():
  print("Python is "+ x)
myfunc()
print("-----------------local Variable----------------")
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is "+ x)
print("-----------------the global keyword----------------")
#If you use the global keyword, the variable belongs to the global scope:
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
print(x)
myfunc()
print("Python is "+ x)
print("-----------------Built-in Data Type----------------")
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = "Hello World"
x = 49
x = 39.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "john", "age":36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
x = None

x = str("Hello World")
x = int(39)
x = float(39.3)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(4)
x = dict(name="john", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(3)
x = bytes(4)
x = bytearray(3)
x = memoryview(bytes(5))

print("-----------------python numbers----------------")
x = 1
y = 3.3
z = 1j
print(type(x))
print(type(y))
print(type(z))
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Complex numbers are written with a "j" as the imaginary part:
