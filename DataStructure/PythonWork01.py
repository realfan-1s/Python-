import math
import time


def Find_Math():
    num = int(input("请输入一个数字: "))
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            print("this %d is not prime number" % num)
            break
    else:
        print("this %d is prime number" % num)


def Change_Word_Method01(word1, word2):
    alist = list(word2)
    pos1 = 0
    stillOK = True
    while pos1 < len(word1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if word1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found == True:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 += 1
    return stillOK


def Change_Word_Method02(word1, word2):
    startTime = time.time()
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    pos1 = 0
    isFound = True
    while pos1 < len(list1) and isFound:
        if list1[pos1] == list2[pos1]:
            pos1 += 1
        else:
            isFound = False
    endTime = time.time()
    RunTime = endTime - startTime
    return isFound, RunTime


def RankNum(word1, word2):
    s1 = [0] * 26
    s2 = [0] * 26
    for i in range(len(word1)):
        pos = ord(word1[i]) - ord('a')
        s1[pos] += 1
    for p in range(len(word2)):
        pos = ord(word2[i]) - ord('a')
        s2[pos] += 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if s1[j] == s2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK


print(RankNum('python', 'typhon'))