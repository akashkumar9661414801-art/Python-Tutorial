word="Python"
with open ("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/log.txt","r") as f:
    lines=f.readlines()
lineno=1
for line in lines:
    if word.lower() in line:
        print(f"Yes python is present {lineno}")
        break 
    lineno+=1
else:
    print("No python is not present ")
'''Here it breaks when it get the word python '''