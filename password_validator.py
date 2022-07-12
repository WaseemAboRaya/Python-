import colorama

def printresult(s:str):
    r=goodpass(s)
    if r:print(colorama.Fore.GREEN+"the pass is good")
    else :print(colorama.Fore.RED+"the pass is not good")
def goodpass(s:str) -> bool:
    Cap, small, numbers, c = 0, 0, 0, 0
    for ch in s:
        c += 1
        if 'Z' >= ch >= 'A': Cap += 1
        if 'z' >= ch >= 'a': small += 1
        if '9' >= ch >= '0': numbers += 1
        if Cap > 0 and small > 0 and numbers > 0 and c >= 10: return True
    return Cap > 0 and small > 0 and numbers > 0 and c >= 10


s1 = "asfrdFasc152"
s2 = "a12548521d545"
s3 = "waAs98"
printresult(s1)
printresult(s2)
printresult(s3)