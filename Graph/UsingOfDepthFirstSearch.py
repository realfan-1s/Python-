from pythonds.graphs import PriorityQueue, Vertex, Graph
import sys


# TopologicalSort拓扑排序
"""
从工作流程图到工作次序排列的算法，称为拓扑排序
将工作流程建立为图，工作项是节点，依赖关系是有向边
最后按照顶点的结束时间从大到小排序，输出这个次序下的顶点列表
"""

# 强连通分支
"""
强连通分支定义为图G的一个分支C，C中的任意两个顶点v,w之间有路径来回，即(v,w)(w,v)都是c的路径，而且c是具有这种特性的最大子集
Transportation转置，一个有向图G的转置G^T,定义为将图G所有有向边都交换次序；如将(v,w)转换为(w,v)
Kosaraju算法：
1.首先对图G调用DFS算法，为每个顶点计算结束时间
2.然后将图G进行转置，得到G^T
3.在对G^T调用DFS算法，但在DFS函数中，对每个顶点的搜索循环中，要以顶点结束时间的倒序为顺序进行搜索
4.最后，深度优先森林的每一棵树就是一个强连通分支
"""

# 最短路径问题
"""
互联网的路由器体系表示为一个带权边的图，路由器作为顶点，路由器的网络链接作为边
Dijkstra算法，是一个迭代算法，得出从一个顶点到其他所有顶点的最短路径算法，很接近BFS算法
具体实现上，在顶点Vertex类上增加一个成员dist用来记录开始顶点到本顶点最短带权路径长度
"""


def Dijkstra(aGraph, start):
    """
    1.顶点的访问次序由一个优先队列来控制，队中的优先级排序由顶点的dist属性来控制
    2.最初，只有开始顶点的dist设置为0，其余顶点的优先级设置为最大整数sys.maxsize
    3.随着队列中每个最低dist的顶点率先出队，并计算该顶点的邻接顶点的权重，会引起其他顶点dist的变化，引发堆重排
    4.根据重拍后的优先队列依次出队
    注意：此算法只能用来处理权重大于零的图，若图中存在权重为负的节点，就会陷入无限循环之中；时间复杂度是O((|V|+|E|)*log|V|)
    """
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)
        

# 最小生成树(Prim算法)
def Prim(G, start):
    """
    生成树：保留有图中所有顶点和最少数量的边，以确保联通的子图
    图G(V,E)的最小生成树T，定义为包含所有顶点V，以及E的无圈子集并且边权重之和最小
    构造最小生成树的方式：若T还不是最小生成树，则反复做：找到一条最小权重的可以安全添加(一端顶点在树中，另一端不在树中)的边，将边添加到树T中去
    """
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newWight = currentVert.getWeight(nextVert)
            if nextVert in pq and newWight < nextVert.getDistance():
                nextVert.setDistance(newWight)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newWight)


"""
最短距离Dijkstra算法和最小生成树prim算法的区别非常相似，稍不留意就会造成混淆。
首先，两个算法都是利用优先队列实现，都是典型的贪心策略算法。
其次，都是以一个无向图G，起始定点start，作为参数。
其算法程序框架几乎一样，不同点如下：
1，Dijkstra算法利用节点的dist属性来记录节点到起始节点的最短权重距离，而prim算法则利用节点的dist属性来记录节点到已建树节点集合的最小权重代价；
2，Dijkstra算法每次从优先队列提取的是到起始节点最短权重距离的节点作为当前节点，而prim算法每次从优先队列提取的是到已建树节点集合最小权重代价的节点作为当前节点；
3，Dijkstra算法遍历当前节点的每一个邻接节点，如果当前节点最短权重距离加上邻接边权重，比邻接节点已有的最短权重距离还短，那就更新邻接节点的最短权重距离和前驱；
prim算法遍历当前节点的每一个安全邻接节点（不在已建树节点集合里），如果当前节点到安全邻接节点的权重，比安全邻接节点已有的最小权重代价还小，那就更新安全邻接节点的最小权重代价和前驱；
4，Dijkstra算法执行完毕后，每个节点的dist记录了到起始节点的最短距离，pred记录了最短距离路径的前驱节点；
prim算法执行完毕后，每个节点的dist记录了到前驱节点的边权重，pred记录了最小生成树路径的前驱节点，把所有dist求和，就是最小生成树的权重代价。
"""