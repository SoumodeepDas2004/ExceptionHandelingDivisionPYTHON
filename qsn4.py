 
def division(a,b):
    try:
        print(f"division of {a} to {b} is :\n {a/b}")
    except ZeroDivisionError:
        print(" \t ZERO DIVISION IS NOT SUPPORTED \n Check the numbers")
    finally:
        print(" \n PROGRAM EXECUTED")

if __name__=='__main__':
    print("\nInput the numbers respectively for divition\n")
    a=int(input("Enter the first number :"))
    b=int(input("Enter the second number :"))
    division(a,b)



 