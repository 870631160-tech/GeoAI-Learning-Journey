import random

target = random.randint(1, 100)
count = 0

print("欢迎来到猜数字游戏！我心里想了一个 1 到 100 之间的数字。")

while True:
    guess = int(input("请输入你猜的数字："))
    
    # 你的代码1：次数加一
    # 你的代码2：判断大小
    # 你的代码3：猜对后 print 和 break      
    count+=1
    if guess < target:
        print("太小了啦！！！")
    elif guess > target:
        print("太大了啦！！！")
    else:
        print(f"猜对啦，一共猜了{count}次")
        break