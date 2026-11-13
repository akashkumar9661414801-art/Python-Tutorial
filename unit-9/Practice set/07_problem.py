word="Python"
with open ("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/log.txt","r") as f:
    lines=f.readlines()
for num,line in enumerate(lines,start=1):
    if word.lower()in line:
        print(f"Python is present in line {num}")
    else:
        print(f"Python is not present in a line {num}")
