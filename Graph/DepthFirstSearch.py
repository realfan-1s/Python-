
"""
首先先将合法走棋次序表示为一个图
采用图搜索算法搜寻一个长度为(行*列-1)的路径，路径上包含每个顶点恰一次
"""
from pythonds.graphs import Graph, Vertex


def GenLegalMoves(x, y, bdSize):
    newMoves=[]
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if LegalCoord(newX, bdSize) and LegalCoord(newY, bdSize):   
            newMoves.append((newX, newY))

    return newMoves


def LegalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    

def KnightGraph(bdSize):
    knightGraph = Graph()
    # 遍历每个格子
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = PosToNodeId(row, col, bdSize)
            newPositions = GenLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = PosToNodeId(e[0], e[1], bdSize)
                knightGraph.addEdge(nodeId, nid)

    return knightGraph


def PosToNodeId(x, y, bdSize):
    return x * bdSize + y


# 深度优先搜索的特点是沿着树的一个单支，向下搜索，只有在无法深入的情况下，还没能找到问题的解，就要回溯上一层再搜索下一支
def DepthFirstSearchForKnightTravel(n, path, u, limit):
    """
    专门用于解决其实搜索问题的算法，每个顶点仅允许访问一次
    引入一个栈来记录路径，并允许进行回溯操作 
    n：层次，path：路径，u:当前顶点，limit：搜索深度
    时间复杂度为O(k^N)
    """
    u.setColor('gray')
    path.append(u)
    if n < limit:
        done = False
        # 获取所有的合法移动
        nbrList = Warnsdorff(u)
        i = 0
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = DepthFirstSearchForKnightTravel(n + 1, path, nbrList[i], limit)
            i += 1
            if not done:
                path.pop()
                u.setColor("white")
    else:
        done = True
    return done


def Warnsdorff(n):
    """
    骑士周游问题算法改进,启发式规则
    """
    resList =[]
    for v in n.getConnections():
        if v.getColor == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor == "white":
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


class UniversalDFS(Graph):
    """
    通用的深度优先搜索算法，允许顶点重复访问，是其他图算法的基础,有时深度优先搜索算法可能会创建多个树
    深度优先搜索算法同样要用到顶点的"前驱"属性来构建森林，此外还要设置发现时间与结束时间
    时间复杂度是O(|V|+|E|)
    """
    def __init__(self):
        super().__init__()
        self.time = 0

    def DFS(self):
        for aVert in self:
            aVert.setColor("white")
            aVert.setPred(-1)
        for aVert in self:
            if aVert.getColor() == "white":
                self.DFSVisit(aVert)

    def DFSVisit(self, startVertex):
        startVertex.setColor("gray")
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor == "gray":
                nextVertex.setPred(startVertex)
                self.DFSVisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)