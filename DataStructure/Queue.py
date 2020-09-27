import random


class Queue:
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def Enqueue(self, item):
        self.items.insert(0, item)

    def Dequeue(self):
        return self.items.pop()

    def Size(self):
        return len(self.items)


def TransferPotato(nameList, num):
    simqueue = Queue()
    for name in nameList:
        simqueue.Enqueue(simqueue)

    while simqueue.Size() > 1:
        for i in range(num):
            simqueue.Enqueue(simqueue.Dequeue())
        simqueue.Dequeue()

    return simqueue.Dequeue()


# 假设学生每小时会提交20页作业,即每隔180s就会有一个作业生成并提交
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def Busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def Tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            self.currentTask = None

    def StartNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.GetPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def GetPages(self):
        return self.pages

    def GetStamp(self):
        return self.timestamp

    def WaitTime(self, currentTime):
        return currentTime - self.timestamp


def NewPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def Simulation(numSeconds, pagePerMinute):
    labPrint = Printer(pagePerMinute)
    printQueue = Queue()
    waitingTimes = []

    # 模拟时间的流逝
    for currentTimes in range(numSeconds):

        # 调用生成作业
        if NewPrintTask():
            task = Task(currentTimes)
            printQueue.Enqueue(task)

        # 打印机打印过程
        if (not labPrint.Busy()) and (not printQueue.IsEmpty()):
            nextTask = printQueue.Dequeue()
            waitingTimes.append(nextTask.WaitTime(currentTimes))
            labPrint.StartNext(nextTask)

        labPrint.Tick()

    averageTime = sum(waitingTimes) / len(waitingTimes)
    print("平均等待时间是 %6.2f 秒，还剩余 %d 个作业未完成" % (averageTime, printQueue.Size()))


for i in range(100):
    Simulation(3600, 10)