def readFile(fileName):
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

lines = readFile("Day4Input.txt")
