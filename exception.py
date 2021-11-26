try:
    a = int(input("Enter a Number"))
    b = int(input("Enter a Number"))
    d = a/b
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by 0!!!")
except ValueError as e:
    print(e)
    print("Enter only Numbers!!!")
except Exception as e:
    print(e)
    print("Some Error occured !!!")
else:
    print(d)
finally:
    print("Execution Sucessfull")