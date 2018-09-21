#ToDo
#Read from file:+
#Sort alphabetically
#Percentage
#Cyrillic symbols only
#Reduction to the general register:+

def sol():
    stringl=string.lower()	
    length=len(stringl)
    dic={}
    for x in stringl:
        dic[x]=stringl.count(x)
    print(dic)

print("Choose a mode:")
print("1-Manual input")
print("2-Read from file")
mode=input()

if mode=="2":
    name=input("Input file name: ")
    file = open(name+'.txt', 'r')
    string=file.read()
    sol()
elif mode=="1":
    string=(input("Input string: "))
    sol()
else:
    print("Wrong mode") 
