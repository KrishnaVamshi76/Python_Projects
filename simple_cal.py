'''write a simple Write a program that takes two numbers 
and an operator (+, -, *, /) as input and performs the corresponding operation.'''

a=int(input("Enter the First Number:\n"))
b=int(input("Enter the second Number:\n"))
operator=input("Select among these operators +,-,*,/")

if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)