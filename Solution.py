import re

def coun(stringl,length):
    dic={}
    sordic={}
    for x in stringl:
        dic[x]=stringl.count(x), str(round(stringl.count(x)/length*100,1))+" %"
    for key in sorted(dic):
        sordic[key]=dic[key]
    print(sordic)
    print("Save result? (Y/N):")
    savemode=input()
    if savemode=="Y":
        savename=input("Input file name: ")
        file = open(savename+'.txt', 'w')
        file.write(str(sordic))
        file.close()
        print("Result save.")
    
def sol():
    stringl=string.lower()	
    length=len(stringl)
    stringl=stringl.replace(" ","")
    stringl = re.sub(u'[^а-я\s]*', u'', stringl)
    lengthcyr=len(stringl)
    if lengthcyr==0:
        print("File or string is empty or do not contain сyrillic symbols.")
    elif lengthcyr>10000:
        print("Await. The program works.")
        coun(stringl,length)
    else:
        coun(stringl,length)

print("Choose a mode:")
print("1-Manual input")
print("2-Read from file") #Only ANSI files.
mode=input()

if mode=="2":
    try:
        name=input("Input file name: ")
        file = open(name+'.txt', 'r')
        string=file.read()
        file.close()
        sol()
    except FileNotFoundError:
        print("Error. File not exist.")
    except PermissionError:
        print("Error. Problems with access to file.")
        
elif mode=="1":
    string=(input("Input string: "))
    sol()
else:
    print("Wrong mode.") 
