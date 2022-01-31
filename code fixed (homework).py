def stringReverse(aString):
 rString = ''
 index = len(aString)
 while index > 0:
    rString += aString[ index - 1 ]
    index = index - 1
 print(rString)
string1 = "Hello World"
print("Original String =", string1)
print("")
print("After Reverse = ")
print(stringReverse(string1))