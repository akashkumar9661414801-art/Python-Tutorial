marks={"akash":50,
      "vikas":45,
      "shubham":67,
}
print(marks.items())#returns a list of (key,value) tuples
print(marks.keys())#returns a keys in list
print(marks.values())#returns a values of a list
print(marks.get("akash"))#Gets a value using a key
marks.update({"Harry":56})#Adds or updates entries
print(marks)
marks.pop("akash")#remove a specific key
print(marks)
marks.popitem()#remove the last inserted pair
print(marks)
#marks.clear()# empty the dictionary
#print(marks)
new_marks=marks.copy()#copy a dictionary
print(new_marks)

