from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename
import re
import sys
sys.path.insert(0, './compilerPhases')
from target import genAssembly, writeassembly

def getFileContent(filePath):
    inputFile = open(filePath, "r")
    return inputFile.readlines()

def writeToOutput(filePath, lines):
    outputFile = open(filePath, "w+")
    outputFile.writelines(lines)

def preProcessLines(lines):
    operators = ["=","-","+","/","*","%","^"]
    # removing spaces
    for li,l in enumerate(lines):
        ltemp = ""
        for c in l:
            if c !=" ":
                ltemp += c
        # substitute ++ for +1 and -- for -1
        for op in ["++","--"]:
            ltemp = list(ltemp)
            for uci, uc in enumerate(ltemp[1:]):
                if "".join(ltemp[uci-1:uci+1]) == op:
                    ltemp[uci-1] = "1"
                    ltemp[uci] = op[0]

            ltemp = "".join(ltemp)
        lines[li] = ltemp
    return lines


# main code, gets file path and compiles it to output
tk().withdraw()
inputFilePath = askopenfilename()
fout = open("out.txt","w")
lines = getFileContent(inputFilePath)
print("Generating Assembly ... ")
vardec, stmt = genAssembly(lines, fout)
print("Assembly Code Generated")
print("Writing to File")
print("---------------")
writeassembly(stmt, vardec, fout)
print("---------------")
print("Compilation Succesful")