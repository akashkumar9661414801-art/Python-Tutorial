import datetime
today=datetime.date.today()
name=str(input("Enter your Name: "))
print(f"Dear A{name}\nyou are selected \n{today}")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>",name).replace("<|Date|>",str(today)))
print(type(today))