def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def Div(a,b):
    return a/b

print("=====WELCOME TO MY CALCULATOR=====")
print()
print("Select Your Operations :")
print("1.Addition (+) :")
print("2.Substraction (-) :")
print("3.Multiplication (*) :")
print("4.Division (/) :")

print()

user=int(input("Enter You'r Operations to perform :"))
print()

number1=int(input("Enter the Number :"))
number2=int(input("Enter the Number :"))



if user==1:
    print(f"The addition of {number1} + {number2} = {add(number1,number2)}")
elif user==2:
    print(f"The substraction of {number1} - {number2} = {sub(number1,number2)}")
elif user==3:
    print(f"The Multiplication of {number1} * {number2} = {mult(number1,number2)}")
elif user==4:
    print(f"The Division of {number1} / {number2} = {Div(number1,number2)}")

else:
    print("invalid selection")
