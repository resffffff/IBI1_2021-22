import re
def replaceStr(oldStr, char, index):  # 在task1-4中均有使用的string替换方法
    newStr = oldStr[:index] + char + oldStr[index+1:]
    return newStr
print(replaceStr('AGTTT','T',1,))