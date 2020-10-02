# 1. 冒泡排序的核心在于对无序表进行多趟排序和交换,经过n-1趟比较，实现整表排序
# 时间复杂度是O(n^2)，空间复杂度O(1)
import timeit


def BubbleSort(alist):
    # 进行交换的趟数
    for passNum in range(len(alist) - 1, 0, -1):
        for i in range(passNum):
            if alist[i] > alist[i + 1]:
                # 错序交换
                # temp = alist[i]
                # alist[i] = alist[i + 1]
                # alist[i + 1] = temp
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


bubbleList = [10, 53, 99, 81, 46, 20, 194]
BubbleSort(bubbleList)
print(bubbleList)


# 2.冒泡排序的性能改进
# 短路的优势高度依赖于数据的初始布局，若初始数据过于随机，造成每趟都有比对的话，该算法完全不具有优势
# 反而要花费生成exchange的性能损耗
def ShortBubbleSort(alist):
    exchange = True
    passNum = len(alist)
    while passNum > 0 and exchange:
        exchange = False
        for i in range(passNum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passNum -= 1


# 3.选择排序算法，保留了冒泡排序多趟对比的思路，每趟都使当前最大项就位
# 比对复杂度为O(n^2),交换次数复杂度减小到O(n),空间复杂度O(1)
def SelectionSort(alist):
    for fillSlot in range(len(alist) - 1, 0, -1):
        maxPosition = 0
        for i in range(1, fillSlot + 1):
            if alist[i] > alist[maxPosition]:
                maxPosition = i

        temp = alist[maxPosition]
        alist[fillSlot] = alist[maxPosition]
        alist[maxPosition] = temp


# 4.插入排序算法,插入排序会维持一个已经排序好了的子列表，其位置始终在列表前部，然后逐步扩大这个子列表至全表
# 比对主要是用来寻找新项和插入位置
def InsertionSort(alist):
    for i in range(1, len(alist)):
        # 取出新项/插入项
        currentValue = alist[i]
        position = i
        while position > 0 and alist[position - 1] > currentValue:
            # 比对、移动
            alist[position] = alist[position - 1]
            position -= 1

        # 插入新项
        alist[position] = currentValue


# 5.希尔排序:对无序表进行间隔划分，每个子列表都执行插入排序
# 间隔逐渐减小，但间隔为一时，执行标准插入排序
# 通常子列表的间隔从n/2开始，渐次减小为n/4，n/8...直到间隔为1
def GapInsertSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentValue


def ShellSort(alist):
    # 设定间隔
    subListCount = len(alist) // 2
    while subListCount > 0:
        for startPositon in range(subListCount):
            GapInsertSort(alist, startPositon, subListCount)
        subListCount //= 2


TestList = [10, 53, 99, 81, 46, 20, 194, 8975, 9, 18]
t1 = timeit.Timer('ShellSort([10, 53, 99, 81, 46, 20, 194, 8975, 9, 18])',
                  'from __main__ import ShellSort')
print("contact", t1.timeit(number=1000), 's')
t2 = timeit.Timer('InsertionSort([10, 53, 99, 81, 46, 20, 194, 8975, 9, 18])',
                  'from __main__ import InsertionSort')
print("contact", t2.timeit(number=1000), 's')


# 6.归并排序——分治策略在排序中的应用
# 空间复杂度是O(logN),时间复杂度是O(NlogN)
def MergeSort(alist):
    """
    1) 基本结束条件：数据表仅有一个数据，自然已经排好序
    2）缩小规模：将数据表分裂成相等的两半
    3）对分成两半的数据表进行归并，得到完成排序的总表
    """
    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]
        # 对左半部分和右半部分的分别进行递归调用
        MergeSort(leftHalf)
        MergeSort(rightHalf)

        # 对完成排序的左半部分与右半部分进行归并
        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i += 1
            else:
                alist[k] = rightHalf[j]
                j += 1
            k += 1

        # 将已经排好序的左右剩余部分添加到队列尾端
        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j += 1
            k += 1


t3 = timeit.Timer('ShellSort([10, 53, 99, 81, 46, 20, 194, 8975, 9, 18])',
                  'from __main__ import ShellSort')
print("contact", t3.timeit(number=10000), 's')


def MergeSortPythonic(alist):
    # 递归结束条件
    if len(alist) <= 1:
        return alist

    # 分解问题并递归调用
    mid = len(alist) // 2
    left = MergeSortPythonic(alist[:mid])
    right = MergeSortPythonic(alist[mid:])

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left if left else right)
    return merged


t4 = timeit.Timer('ShellSort([10, 53, 99, 81, 46, 20, 194, 8975, 9, 18])',
                  'from __main__ import ShellSort')
print("contact", t4.timeit(number=10000), 's')


# 7.快速排序算法——依据中值数据将数据表分为两半，对每一部分进行递归
# 空间复杂度是O(logN) 时间复杂度是O(NlogN)
def QuickSort(alist):
    """
    1.基本结束条件：列表中仅剩下一个数据项，自然已经排好序
    2.缩小规模：依据中值，将数据表分为两半，最佳情况是规模相等的两半
    3.调用自身：将两半分别调用自身进行排序
    """
    QuickSortHelper(alist, 0, len(alist) - 1)


def QuickSortHelper(alist, start, last):
    if start < last:  # 基本结束条件
        splitPoint = Partition(alist, start, last)  # 找到分裂点
        QuickSortHelper(alist, start, splitPoint - 1)
        QuickSortHelper(alist, splitPoint + 1, last)


def Partition(alist, start, last):
    # 选定中值
    pivotValue = alist[start]
    # 左右标中值
    leftPoint = start + 1
    rightPoint = last
    finished = False
    while not finished:
        # 左标向右移动直到左标大于右标或左标对应值大于中值
        while leftPoint <= rightPoint and alist[leftPoint] <= pivotValue:
            leftPoint += 1
        # 右标向左移动直到右标小于左标或右标对应值小于中值
        while rightPoint >= leftPoint and alist[rightPoint] >= pivotValue:
            rightPoint -= 1

        if rightPoint < leftPoint:
            finished = True
        else:
            # 左右标的值相互交换
            temp = alist[leftPoint]
            alist[leftPoint] = alist[rightPoint]
            alist[rightPoint] = temp

    # 中值就位
    temp = alist[start]
    alist[start] = alist[rightPoint]
    alist[rightPoint] = alist[start]

    # 传回中值点
    return rightPoint


# 8.采用三点取中法的快速排序算法
def QuickSort02(alist):
    if len(alist) < 2:
        return alist
    mid = alist[len(alist) // 2]
    pivotValue = sorted([alist[0], mid, alist[-1]]).pop(1)
    left, right = [], []
    alist.remove(pivotValue)
    for item in alist:
        if item < pivotValue:
            left.append(item)
        else:
            right.append(item)

    return QuickSort02(left) + [pivotValue] + QuickSort02(right)


QuickSortList = [10, 53, 99, 81, 46, 20, 194, 8975, 9, 18]
t5 = timeit.Timer('QuickSort02([10, 53, 99, 81, 46, 20, 194, 8975, 9, 18])',
                  'from __main__ import QuickSort02')
print("contact", t5.timeit(number=10000), 's')
