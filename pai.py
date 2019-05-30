import random

# 玩家A
Jack = []
# 玩家B
Bob = []
# 玩家C
Mair = []
# 底牌3张
dp = []

# 玩家列表
gamer = [Jack, Bob, Mair]

#生成扑克牌
def ptp():
    pai = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    leixing = ["♥", "♦", "♠", "♣"]
    king = ["🤴", "👸"]
    commonpai = []
    for k in king:
        commonpai.append(k)
    for p in pai:
        for l in leixing:
            commonpai.append(l+p)
    return  commonpai


#打乱扑克牌
def randompk(c):
    random.shuffle(c)

#发牌
def fp(commonpai):

    Jack.append(commonpai[0:16])
    Bob.append(commonpai[17:33])
    Mair.append(commonpai[34:50])
    dp.append(commonpai[51:54])
    print("".join('玩家Jack:%s' %id for id in Jack))
    print("".join('玩家Bob:%s' %id for id in Bob))
    print("".join('玩家Mair:%s' %id for id in Mair))
    print("".join('底牌3张:%s' %id for id in dp))

#抢地主
def randomgamer(gamer,dp):
    # 打乱玩家抢地主顺序
    random.shuffle(gamer)
    print("".join("第一个抢地主的人是：%s" %p for p in gamer[0]))


    # print(gamer)
    for person in gamer:
        # 是否抢地主
        qdz = input("抢地主？请输入： 抢 or 不抢 ")
        # print(person)
        print(qdz)
        if qdz=="抢":
            print("恭喜你抢到地主！！")
            person+=dp
            print(person)
            break
        elif qdz=="不抢":
            pass
        else:
            input("请重新输入： 抢 or 不抢 ")

#测试
c=ptp()
randompk(c)
fp(c)
randomgamer(gamer,dp)







