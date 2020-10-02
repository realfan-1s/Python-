# 用二叉堆(binary heap)实现优先队列
# 二叉堆特点：逻辑结构上像二叉树，但实现方式是非嵌套列表
# 完全二叉树：叶节点最多只出现在最底层和次底层，而且最底层的叶节点都连续集中在最左边，每个内部节点都有两个子节点，最多有一个例外
# 在完全二叉树的条件下，若某个节点的下标为p，则左子节点的下标为2p，右子节点的下标为2p+1，父节点的下标为p//2
# 任何一个节点x，其父节点p中的key均小于节点x中的key
class BinaryHeap:
    def __init__(self):
        # 为了保留有下标相关联的性质，第0个数据项不使用
        self.heapList = [0]
        self.currentSize = 0

    def PrecUp(self, i):
        """
        为了不破坏二叉堆的次序，新节点必须渐次上浮，与父节点相比，直到大于父节点为止
        """
        needChange = True
        while i // 2 > 0 and needChange:
            if self[i] < self[i // 2]:
                temp = self[i]
                self[i] = self[i // 2]
                self[i // 2] = temp
            else:
                needChange = False
            i //= 2

    def Insert(self, key):
        """
        为了保证完全二叉树的状态，新的插入项不许先添加至末尾
        """
        self.heapList.append(key)
        self.currentSize += 1
        self.PrecUp(self.currentSize)

    def PrecDown(self, i):
        """
        将新的根节点逐渐下沉，直到比两个子节点都要小
        """
        while (2 * i) <= self.currentSize:
            mc = self.MinChild(i)
            if self.heapList[mc] < self.heapList[i]:
                temp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = temp
            i = mc

    def MinChild(self, i):
        """
        获取两个子节点中最小的那个
        """
        if 2 * i + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[2 * i + 1] > self.heapList[2 * i]:
                return 2 * i
            else:
                return 2 * i + 1

    def DelMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.PrecDown(1)
        return retVal

    def BuildHeap(self, alist):
        # 叶节点无需下沉，从叶节点的父节点开始,复杂度为O(n)
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while (i > 0):
            self.PrecDown(i)
            i -= 1
        print(self.heapList, i)
