# randomWallOfCode.py
# Nicolas Hahn

# You know how major news outlets always use a picture of some 
# random wall of meaningless code for any article relating to software?
# This makes one of those.

import random
import sys

def generateLine(w,snippets):
    newSnippets = snippets
    random.shuffle(newSnippets)
    line = ""
    i = 0
    while len(line) < w:
        line += newSnippets[i]
        i += 1
    line = line[:w]
    return line

def main(w=sys.argv[1],h=sys.argv[2],f=sys.argv[3]):
    snippets = []
    with open('snippets.txt','r') as snippetsFile:
        for line in snippetsFile:
            snippets.append(line[:-1])
    h = int(h)
    w = int(w)
    # w = int(input("Width of wall of code in chars:")) 
    # h = int(input("Height of wall of code in chars:"))
    # f = input("File to write to (optional, leave blank for just stdout print):")
    fList = []
    for _ in range(h):
        line = generateLine(w,snippets)
        print(line)
        fList.append(line+'\n')
    if f != "":
        outputFile = open(f,'w')
        [outputFile.write(i) for i in fList]
        outputFile.close()

if __name__ == '__main__':
    main()

