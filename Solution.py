import re
import chardet
import sys

def codecs():
    with open(name+".txt", "rb") as file:
        text = file.read()
        enc = chardet.detect(text).get("encoding")
        file.close()
    if enc!="windows-1251" and enc!="MacCyrillic" and enc!="ISO-8859-8" and enc!="windows-1255":
        print("Wrong encoding.")
        sys.exit()

def coun(stringl,length):
    dic={}
    sordic={}
    for x in stringl:
        dic[x]=stringl.count(x), str(round(stringl.count(x)/length*100,1))+"%"
    for key in sorted(dic):
        sordic[key]=dic[key]
    print(str(sordic).replace("'",""))
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
    stringl=stringl.replace("\n","")
    stringl=stringl.replace("\t","")
    stringl=stringl.replace("\x0","")
    stringl = re.sub(u'[^à-ÿ¸\s]*', u'', stringl)
    lengthcyr=len(stringl)
    if lengthcyr==0:
        print("File or string is empty or do not contain Ñyrillic symbols.")
    elif lengthcyr>10000:
        print("Await. The program work.")
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
        codecs()
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
