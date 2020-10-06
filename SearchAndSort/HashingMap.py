# 散列hashing能将查找的复杂度降低到O(1)
# hash table中的每一个存储位置，称为槽(slot)，可以用来保存数据项
# 常用散列方法——求余数，将数据项除以散列表大小，得到的余数作为槽号
# 槽被数据项占据的比例称为负载因子
# 完美散列函数———若一个函数能够将每个数据映射到不同的槽中，这个散列函数便被称为完美散列函数
import hashlib
str = hashlib.sha256('hello,World!'.encode('utf-8')).hexdigest()
print(str)

m = hashlib.md5()
m.update('hello,World'.encode('utf-8'))
m.update('This is part #2'.encode('utf-8'))
print(m.hexdigest())

# 1.折叠法设计散列函数
"""
1. 将数据项按照位数分为若干段
2. 再将几段数字相加
3. 对散列表大小求余数，得到哈希值
4. 通常还包括了隔数反转
"""

# 2.平方取中法
"""
1. 先将数据项做平方计算
2. 再取平方数的中间两位
3. 再对散列表的大小取余
"""


def CharacterHash(astr, tabSize):
    sum = 0
    for pos in range(len(astr)):
        sum += ord(astr[pos]) * pos
    return sum % tabSize


print(CharacterHash('CAT', 13))
"""
线性探测
为冲突的数据项再寻找一个开放的空槽进行保存
若在散列位置没有找到查找项，就必须向后做顺序查找
缺陷：具有聚集的趋势
rehash(pos) = (pos + 1) % hashsize
可以使用跳跃式探测来避免聚集
rehash(pos) = (pos + skip) % hashsize
"""


class HashTable:
    """
    使用Hash table类来实现ADT Map创建新的映射
    其中一个slot列表用于保存key
    另一个平行的data列表用于保存数据项
    在slot查找到一个key的位置之后，在data列表的相同位置的数据项即为关联数据
    """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.datas = [None] * self.size

    def HashFunction(self, key):
        return key % self.size

    def Rehash(self, oldHash):
        return (oldHash + 1) % self.size

    def Put(self, key, data):
        # 求得散列值hashvalue
        hashValue = self.HashFunction(key)

        # 若key不存在，未冲突
        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.datas[hashValue] = data
        else:
            # 若key已经存在，但不存在对应的数据项
            if self.slots[hashValue] == key:
                self.datas[hashValue] = data
            else:
                # 发生散列冲突，再散列，直到找到空槽或者对应新key
                nextSlot = self.Rehash(hashValue)
                while self.slots[nextSlot] != None and self.slots[
                        nextSlot] != key:
                    nextSlot = self.Rehash(nextSlot)

                if self.slots[nextSlot] is None:
                    self.slots[nextSlot] = key
                    self.datas[nextSlot] = data
                else:
                    self.datas[nextSlot] = data

    def Get(self, key):
        startSlot = self.HashFunction(key)
        data = None
        position = startSlot
        stop = False
        found = False
        # 找key，直到空槽或回到起点
        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                data = self.datas[position]
                found = True
            else:
                position = self.Rehash(position)
                if position == startSlot:
                    # 回到了起点，证明未能找到
                    stop = True
        return data

    def __setitem__(self, key, data):
        self.Put(key, data)

    def __getitem__(self, key):
        return self.Get(key)


"""
1. 若采用线性探测法解决冲突，负载因子λ在0-1之间
成功的查找，平均比对次数为：（1+1/(1-λ)）/2
不成功的查找，平均比对次数为：(1+(1/(1-λ)^2))/2

2. 若采用数据链的方式解决collision
成功的查找，平均比对次数为：1+λ/2
不成功的查找，平均比对次数为：λ
"""