###Write a program to illustrate the use of 'is' identity operator

v=10

if type(v) is int:
    print("true")
else:
    print("false")


s=[1,2,3,4,5,6,7,8,9]
h=[1,2,3,4,5,6,7,6,9]


s=h
print(s is not h)