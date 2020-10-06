import time


# 1. 找零问题算法,'贪心算法'
# 每次都要尽量解决问题中尽量大的一部分，使用递归方法
# 建立查询表，将计算得到的最小硬币数储存在查询表中
def RecMC01(coinList, change, knowResults):
    minCoin = change
    if change in coinList:
        knowResults[change] = 1
        return 1
    # 查表成功，直接获得最优解
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinList if c <= change]:
            coinNum = 1 + RecMC01(coinList, change - i, knowResults)
            if coinNum < minCoin:
                minCoin = coinNum
                # 找到最优解，添加到表中
                knowResults[change] = minCoin
    return minCoin


startTime = time.time()
print(RecMC01([1, 5, 10, 21, 25], 63, [0] * 64))
endTime = time.time()
print(endTime - startTime)


# 2. 动态规划解法
# mincoin记录最小硬币数
def dpMakeChange(coinValueList, change, minCoin):
    # 从1分开始计算最小硬币数
    for cents in range(1, change + 1):
        # 初始化最大值
        coinCount = cents
        # 减去每个硬币，向后查找最小硬币数，同时记录总最少数
        for i in [c for c in coinValueList if c <= cents]:
            if minCoin[cents - i] + 1 < coinCount:
                coinCount = minCoin[cents - i] + 1
        minCoin[cents] = coinCount
    return minCoin[change]


print(dpMakeChange([1, 10, 21, 25], 63, [0] * 64))


# 3. 动态规划算法扩展
def dpMakeChangeExtend(coinValueList, change, minCoin, CoinsUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for i in [c for c in coinValueList if c <= cents]:
            if minCoin[cents - i] + 1 < coinCount:
                coinCount = minCoin[cents - i] + 1
                newCoin = i
        minCoin[cents] = coinCount
        CoinsUsed[cents] = newCoin
    return minCoin[change]


def PrintCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin


amount = 63
coinList = [1, 5, 10, 21, 25]
coinUsed = [0] * (amount + 1)
coinCount = [0] * (amount + 1)
print("num is ", end='')
print(dpMakeChangeExtend(coinList, amount, coinCount, coinUsed))
print("They are ", end='')
print(PrintCoins(coinUsed, amount))


# 4. 博物馆大盗问题
def Steal(tr, max_w):
    """
    初始化二维表格m[(i, w)]
    在前i个表格中，最大重量w下所能获得的最大价值
    """
    m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}
    for i in range(1, len(tr)):
        for w in range(1, (max_w + 1)):
            if tr[i]['w'] > w:
                m[(i, w)] = m[(i - 1, w)]
            else:
                m[(i, w)] = max(m[(i - 1, w)],
                                (m[(i - 1, w - tr[i]['w'])] + tr[i]['v']))

    return m[(len(tr) - 1, max_w)]


tr = [
    None, {
        'w': 2,
        'v': 3
    }, {
        'w': 3,
        'v': 4
    }, {
        'w': 4,
        'v': 8
    }, {
        'w': 5,
        'v': 8
    }, {
        'w': 9,
        'v': 10
    }
]

print(Steal(tr, 20))

Trs = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}
m = {}


def Thief(tr, max_w):
    if tr == set() or max_w == 0:
        m[(tuple(tr), max_w)] = 0
        return 0
    elif (tuple(tr), max_w) == m:
        return m[(tuple(tr), max_w)]
    else:
        vmax = 0
        for t in tr:
            if t[0] <= max_w:
                # 逐个从集合中去掉某个宝物，递归调用
                v = Thief(tr - {t}, max_w - t[0]) + t[1]
                vmax = max(vmax, v)
        m[tuple(tr), max_w] = vmax
        return vmax


print(Thief(Trs, 20))
