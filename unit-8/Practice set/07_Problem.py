
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["Harry","Rohan","Shubham","an"]
print(rem(l,"an"))
b=["anar","dhan","rohana","anus","anaranafan","nagna"]
#bich wala nhi hatega ya to last wala ya fir first wala
#agr "an" hai to ana nana 
print(rem(b,"an"))