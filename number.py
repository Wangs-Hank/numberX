class Calculator:
    pass
################

# 以下为正式代码 #
################

primeList = []
for i in range(2, 10000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primeList.append(i)


def Mersenne(numX):
    prime = []
    for i in range(2, numX):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    print(prime)

# 以下为调用类
# Number为核心库，-x为头的方法都在其中

class Number:
    def __init__(self, num):
        self.num = num

    def InstructionSet_MS(self):
        print("""
    指令：
    以-x为开头的指令通常为程序本身的运行参考
    以-i为开头的指令通常为快捷方法

    -x README
    查看程序
    ----------------------------------
    -x SET 
    查看程序指令集
    ----------------------------------
    -x FILES
    查看程序文件分类与文件运行方式
    ----------------------------------

    -i Mersenne
    穿进一个参数,求从2到参数内所有的质数
    
    ----------------------------------
    
    -i fac
    求一个数的因数
    
    -i -c fac
    求两个数的公因数
    
    -i mtp
    求一个数的倍数
    
    -i -c mtp
    求两个数的公倍数
    
    ----------------------------------
    END
    """)

    def README_MS(self):
        pass

    def FILES_MS(self):
        print("""
    本程序涉及Python和Json语言.
    假设看源码,需安装编辑器及Python环境.
    运行程序直接.exe文件双击打开即可
    ----------------------------------
    源码版本(1.0)
    Python文件3项：
    num.py  ---  (主文件)
    number.py  ---  (类库,函数,方法)
    json_write.py  ---  (json文件写入,如果学过Json直接忽略即可)
    
    Json文件1项：
    ----------------------------------
    key.json
    ----------------------------------
    END
    """)

    def judge(self):
        if self.num % 2 == 0:
            print("{}是偶数".format(self.num))
        else:
            print("{}是奇数".format(self.num))
        if self.num > 1 and self.num in primeList:
            print("{}是素数".format(self.num))
        else:
            print("{}是合数".format(self.num))
# Number_2为

class Number_2:
    def __init__(self):
        pass
    
    # 因数
    def yinshu(self, num):
        yinshuList = []
        for i in range(2, num):
            if num % i == 0:
                yinshuList.append(i)
        print(yinshuList)

    # 倍数
    def beishu(self, num):
        beishuList = []
        for i in range(1, 10):
            beishuList.append(num * i)
        print(beishuList)

    # 公因数
    def gongyinshu(self, num1, num2):
        gongyinshuList = []
        for i in range(2, num1):
            if num1 % i == 0 and num2 % i == 0:
                gongyinshuList.append(i)
        print(gongyinshuList)

    # 公倍数
    def gongbeishu(self, num1, num2):
        num1beishuList = []
        for i in range(1, 1000):
            num1beishuList.append(num1 * i)
        num2beishuList = []
        for i in range(1, 1000):
            num2beishuList.append(num2 * i)
        gongbeishuList = []
        for gongbeishu in num1beishuList:
            if gongbeishu in num2beishuList:
                gongbeishuList.append(gongbeishu)
        print(gongbeishuList)

    # 约瑟夫环
    def yuesefuhuan(self, num1, num2, num3, num4):
        # 编号范围
        totalNumber = num1
        # 开始编号
        startNumber = num2
        # 序号
        orderNumber = num3
        # 删除序号
        outNumber = num4
        # 索引
        index = startNumber - 1

        numList = []
        for i in range(1, totalNumber + 1):
            numList.append(i)

        while True:
            # 如果列表中是一个数据时，筛选结束
            if len(numList) == 1:
                break
            # 如果序号等于删除序号则删除该位置的数据
            if orderNumber == outNumber:
                numList.pop(index)
                orderNumber = 1
            else:
                orderNumber += 1
                index += 1
                # print("index:{}".format(index))

            if index >= len(numList):
                index = 0

        print("The last number is {}".format(numList[0]))


class Number3:
    def __init__(self):
        pass
    
    def huiwenshu(user):
        n = 0
        num = 0
        while True:
            a = int(user) // 10**n % 10
            num = num * 10 +a
            n += 1
            if n == len(user):
                break
        if num == int(user):
            return 1
        else:
            return 0