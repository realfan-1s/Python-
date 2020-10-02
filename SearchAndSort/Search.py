def UnorderedListSequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
            print('您查找的数字位于第 %d 项' % (pos + 1))
        else:
            pos += 1

    return found


def OrderedListSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
            print('您查找的数字位于第 %d 项' % (pos + 1))
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found


# 有序列表查找算法——二分法(分治策略),最差复杂度O(logN)
def BinarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        else:
            if alist[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found


# 二分法递归算法
def BinarySearchRecursion(alist, item):
    first = 0
    last = len(alist) - 1
    if len(alist) == 0:
        return False
    else:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return BinarySearch(alist[:mid], item)
            else:
                return BinarySearch(alist[mid + 1:], item)