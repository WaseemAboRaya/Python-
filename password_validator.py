import sys

def printresult(s: str) -> bool:
    r = goodpass(s)
    if r:
        print('\033[32m' + " the pass is good")
        return 0
    else:
        return 1


def goodpass(s: str) -> bool:
    if s == "":
        print('\033[1;32;40m' + " the pass is empty")
        return False
    Cap, small, numbers, c = 0, 0, 0, 0
    for ch in s:
        c += 1
        if 'Z' >= ch >= 'A': Cap += 1
        if 'z' >= ch >= 'a': small += 1
        if '9' >= ch >= '0': numbers += 1
        if Cap > 0 and small > 0 and numbers > 0 and c >= 10: return True
    if c < 10: print('\033[31m' + " Length – minimum of 10 characters")
    if Cap == 0: print('\033[31m' + " there are no capital letters")
    if small == 0: print('\033[31m' + " there are no small letters")
    if small == 0: print('\033[31m' + " there are no number letters")
    return Cap > 0 and small > 0 and numbers > 0 and c >= 10


try:
    x = sys.argv[1]
    if x == "MyP@ssw0rd!":
        with open('expass.txt', 'r') as f:
            for x in f.readlines():
                print("the pass in file is :",x)
                r1 = printresult(x)
                print(r1)
    else:
        print("There is something missing")
except:
    print("An exception occurred, There is something missing")
