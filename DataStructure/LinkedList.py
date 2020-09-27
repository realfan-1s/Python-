# 链表的链首和链尾需要被特别标记出来
# 无序链表插入最快捷的位置是表头
class node:
    def __init__(self, initdata):
        """
        设置初始链表
        """
        self.data = initdata
        self.next = None

    def GetData(self):
        """
        获取当前项
        """
        return self.data

    def GetNext(self):
        """
        获取下一项
        """
        return self.next

    def SetData(self, newData):
        self.data = newData

    def SetNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        """
        初始化无序表
        """
        self.head = None

    def IsEmpty(self):
        return self.head is None

    def Add(self, item):
        """
        为链表添加元素
        要非常小心链表的次序
        """
        temp = node(item)
        temp.SetNext(self.head)
        self.head = temp

    def Size(self):
        """
        从链条头head开始遍历到表尾
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.GetNext()
        return count

    def Search(self, item):
        current = self.head
        isFound = False
        while current != None and not isFound:
            if current.GetData() == item:
                isFound = True
            else:
                current = current.GetNext()
        return isFound

    def Remove(self, item):
        """
        移除链表中的某个节点
        """
        current = self.head
        previous = None
        isFound = False
        while not isFound:
            if current.GetData() == item:
                isFound = True
            else:
                previous = current
                current = current.GetNext()

        if previous == None:
            self.head = current.GetNext()
        else:
            previous.SetNext(current.GetNext())


class OrederedList:
    """
    有序列表抽象数据类型
    数据项的相对位置，取决于他们的大小对比
    在python中，可以适用于所有定义了__gt__(即‘(’)的数据类型
    """
    def __init__(self):
        """
        生成一个空的有序列表
        """
        self.head = None

    def IsEmpty(self):
        """
        判断是否为空
        """
        return self.head is None

    def Size(self):
        """
        返回链表的个数
        """
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.GetNext()
        return count

    def Remove(self, item):
        """
        移除元素
        """
        isFound = False
        previous = None
        current = self.head
        while not isFound:
            if current.GetData() == item:
                isFound = True
            else:
                previous = current
                current = current.GetNext()

        if previous == None:
            self.head = current.GetNext()
        else:
            previous.SetNext(current.GetNext())

    def Search(self, item):
        """
        搜索元素
        在有序表中，可以利用链表节点有序排列的特性，
        一旦发现当前数据项大于要查找的数据项，就可以停止查找,直接返回False
        """
        current = self.head
        isFound = False
        stop = False
        while current != None and not isFound and not stop:
            if current == item:
                isFound = True
            else:
                if current > item:
                    stop = True
                else:
                    current = current.GetNext()

        return isFound

    def Add(self, item):
        """
        添加元素，并且维持链表的有序性
        """
        previous = None
        current = self.head
        isStop = False
        while current != None and not isStop:
            if current > item:
                isStop = True
            else:
                previous = current
                current = current.GetNext()

        temp = node(item)
        if previous == None:
            temp.SetNext(self.head)
            self.head = temp
        else:
            temp.SetNext(current)
            previous.SetNext(temp)