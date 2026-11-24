'''(n := len([1, 2, 3, 4, 5])) > 3 this means 
n=len([1, 2, 3, 4, 5] and n>3'''
# Using Walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
 print(f"List is too long ({n} elements, expected <= 3)")