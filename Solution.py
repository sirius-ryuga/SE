# -*- coding: utf-8 -*-

import re
import chardet
import sys

def codecs(filename):
    with open(filename, "rb") as file:
        text = file.read()
        return chardet.detect(text).get("encoding", "ascii")

def coun(stringl,length):
    dic={}
    for x in stringl:
        dic[x]=stringl.count(x), str(round(stringl.count(x)/length*100,1))+"%"
    dic = {key: dic[key] for key in sorted(dic)}
    print(str(dic).replace("'",""))
    print("Save result? (Y/N):")
    savemode=input()
    if savemode=="Y":
        savename=input("Input file name: ")
        file = open(savename, 'w')
        file.write(str(dic))
        file.close()
        print("Result save.")
    
def sol(string):
    stringl=string.lower()	
    length=len(stringl)
    stringl = re.sub(u'[^а-яё]*', u'', stringl)
    lengthcyr=len(stringl)
    if lengthcyr==0:
        print("File or string is empty or do not contain cyrillic symbols.")
    elif lengthcyr>10000:
        print("Await. The program work.")
        coun(stringl,length)
    else:
        coun(stringl,length)

def main():
    print("Choose a mode:")
    print("1-Manual input")
    print("2-Read from file")
    mode=input()

    if mode=="2":
        try:
            name=input("Input file name: ")
            encoding = codecs(name)
            string = None
            with open(name, 'r', encoding=encoding) as file:
                string=file.read()
            sol(string)
        except FileNotFoundError:
            print("Error. File not exist.")
        except PermissionError:
            print("Error. Problems with access to file.")
            
    elif mode=="1":
        string=(input("Input string: "))
        sol()
    else:
        print("Wrong mode.") 

if __name__ == '__main__':
    main()
