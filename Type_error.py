try:
    num1=int(input("Enter any value."))
    num2=int(input("enter any value."))

    result=num1+num2

    print(result)

except TypeError:
    print("Error:string and numeric value cannot be addded")

