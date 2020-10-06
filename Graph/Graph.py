"""
基本组成：1.vertex（顶点），是图的基本组成部分，顶点具有名称标识key，也可以携带数据项payload
2.edge(边)/Arc(弧)作为两个顶点之间关系的表示，边连接两个顶点，边可以是有向的，也可是无向的
3.权重(weight),表示从一个顶点到另一个顶点的代价，可以给边赋权
一个图G可以定义为G=(V,E)的集合，其中V是顶点的集合，E是边的集合，E中的每条边e=(v,w),v、w都是V中的顶点；若是赋权图，则还可以在e中添加权重分量
4.路径(path)是由边依次连接起来的顶点序列；无权路径的长度是边的数量，有权路径的长度是所有路径权重之和
5.圈(Cycle)圈是首尾相连的路径；若图中不存在任何的圈，称为有向无圈图
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def AddNeighber(self, nbr, weight=0):
        # 添加边,nbr是顶点对象的key
        self.connecTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connect to: ' + str([x.id for x in self.connectTo]) 

    def GetConnetions(self):
        return self.connectTo.keys()

    def GetId(self):
        return self.id

    def GetWeight(self, nbr):
        # 返回所连接顶点的权重
        return self.connectTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def AddVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def GetVertex(self, key):
        # 通过key查找顶点
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def AddEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.AddVertex(f)
        if t not in self.vertList:
            nv = self.AddVertex(t)
        
        self.vertList[f].AddNeighber(self.vertList[t], cost)

    def GetEdge(self):
        # 获取途中包含的所有顶点
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

   
