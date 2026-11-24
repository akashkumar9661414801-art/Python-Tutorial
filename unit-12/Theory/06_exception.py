try:
    a=int(input("Enter the number: "))
    print(a)
except ValueError as v:
    print("value error")
    print(v)
except Exception as e:
    print(e)
print("Thank you")