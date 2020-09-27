# 双端队列，数据项既可以从队首加入，也可以从队尾加入；数据项同样可以从两端移除
# 双端队列集成了栈和队列的特性
class Deque:
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    # 将数据项加入队首
    def AddFront(self, item):
        self.items.append(item)

    # 将数据项从队尾加入,复杂度O（n）
    def AddRear(self, item):
        self.items.insert(0, item)

    # 将数据项从队首移除,复杂度O(1)
    def RemoveFront(self):
        return self.items.pop()

    # 将数据项从队尾移除，复杂度O(n)
    def RemoveRear(self):
        return self.items.pop(0)

    def Size(self):
        return len(self.items)


# 回文词判定
def palChecker(aString):
    charDeque = Deque()
    stillEqual = True

    for ch in aString:
        charDeque.AddFront(ch)

    while charDeque.Size() > 1 and stillEqual:
        first = charDeque.RemoveFront()
        last = charDeque.RemoveRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(palChecker('lsdoio'))
print(palChecker('toot'))