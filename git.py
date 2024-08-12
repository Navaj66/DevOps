print("Hello")
#calculator
Num1=int(input("Enter no.1= "))
operator=input("Enter operator(+,-,*,/) = ")
Num2=int(input("Enter no.2= "))

if operator== "+":
    print(Num1 + Num2)

elif operator== "-":
    print(Num1 - Num2)

elif operator== "*":
    print(Num1 * Num2)

elif operator== "/":
    if Num2 !=0:
        print(Num1 / Num2)
    else:
        print("Divided by zero is indefinite so kindly remove zero from Num1 ")   
    
else:
    print( "Enter valid Opeartor" )
