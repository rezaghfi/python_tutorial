
print("______________________________python functions______________________________")
# print("Hello it is simple calculator\n Enter your input1:")
# input1 = int(input())
# print("Enter your input2:")
# input2 = int(input())
# def add(in1, in2): return in1 + in2
# def sub(in1, in2): return in1 - in2
# def mul(in1, in2): return in1 * in2
# def div(in1, in2): return in1 / in2
# print(" add input1 and input2 is:",add(input1, input2))
# print(" sub input1 and input2 is:",sub(input1, input2))
# print(" multiple input1 and input2 is:",mul(input1, input2))
# print(" division input1 and input2 is:",div(input1, input2))

def drawRectangle(row):
  i = 1
  while i <= row:
    j = 1
    while j <= i:
      print('*', end = ' ')
      j += 1
    i += 1
    print("")

drawRectangle(5)