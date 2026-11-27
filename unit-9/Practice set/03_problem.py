'''3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
files. Place these files in a folder for a 13-year-old.'''
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n}X{i}={n*i}\n"
    print(f"C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/Tables/table_{n}.txt"+" Creating")
    with open(f"C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/Tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):      # no spaces before "for"
    generateTable(i)