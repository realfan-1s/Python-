from Graph.Graph import Graph
from DataStructure.Queue import Queue
# 词梯问题
"""
1. 采用暴力解算，对每个顶点与其他所有单词进行比较，若只相差一个字母，便建立一条边，此时的时间复杂度是O(n)
2. 改进算法是创建一个桶，每个桶内可以存放多个单词，所有匹配标记的单词可以放到桶内,所有单词就位后，再在每个单词间建边即可
"""


def BuildGraph(wordFile):
    # 最大时间复杂度为O(V^2)
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # 创建桶以存放单词
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # 在同一个桶内为单词创建顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.AddEdge(word1, word2)

    return g


def BreadthFirstSearch(g, start):
    """
    给定图G，以及开始的起点s，BFS搜索所有从s可以到达顶点的边
    在到达更远距离k+1的顶点之前，BFS会找到所有距离为k的顶点
    为了避免重复，要为顶点增加三个属性：
    (1) 距离distance：从起始顶点到此顶点的长度路径
    (2) 前去顶点Predecessor：可以反向追溯到起点
    (3) 颜色Color：未发现是白色，已经发现为灰色，完成搜索为黑色
    还需要一个队列对已发现的顶点进行排列,综上时间复杂度是O(|v|+|E|)
    """
    start.SetDistance(0)
    start.SetPred(None)
    vertQueue = Queue()
    vertQueue.Enqueue(start)
    # 取出队首作为顶点
    while (vertQueue.Size > 0):
        currentVert = vertQueue.Dequeue()
    # 遍历临界顶点
    for nbr in currentVert.GetConnections():
        if (nbr.GetColor() == "white"):
            nbr.SetPred(currentVert)
            nbr.SetColor("grey")
            nbr.SetDistance(currentVert.GetDistance() + 1)
            vertQueue.Enqueue(nbr)

    currentVert.SetColor("black")
    

def Traverse(y):
    x = y
    while (x.GetPred()):
        print(x.GetID())
        x = x.GetPred()
    print(x.GetID())



