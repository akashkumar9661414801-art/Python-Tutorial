n=int(input("Enter a number "))
table=[]

table=[i*n for i in range(1,11)]
print(table)
with open("C:/python/pythoncourse/Python-Tutorial/unit-12/Practice Set/tables.txt","a")as f:
    f.write(f"{str(table)}\n")
