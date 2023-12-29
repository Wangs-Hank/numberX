import time

import json
from pathlib import Path

from number import Number
from number import Number_2
from number import Mersenne
from number import Calculator

# while True:
#     print('check the key...')
#     time.sleep(0.5)
#     try:
#         path_key = open('key.json')
#     except:
#         print('key is not defined')
#     else:
#         print('Welcome to numberX')
#         break

print('Welcome to numberX')
while True:
    Set = input(">")
    try:
        num = int(Set)
    except:
        if Set == 'quit':
            break
        
        elif Set == "-x SET":
            number = Number()
            number.InstructionSet_MS()

        elif Set == "-x README":
            number = Number()
            number.README_MS()

        elif Set == "-x FILES":
            number = Number()
            number.FILES_MS()


        # number 2.0
        # 因数，倍数，约瑟夫环
        # 公倍数，公因数
        elif Set == "-i fac":
            try:
                num = int(input("<"))
            except:
                print("It isn't a number.")
            else:
                number = Number_2()
                number.yinshu(num)

        elif Set == "-i mtp":
            try:
                num = int(input("<"))
            except:
                print("It isn't a number.")
            else:
                number = Number_2()
                number.beishu(num)

        elif Set == "-i -c fac":
            try:
                num1 = int(input("<"))
                num2 = int(input("<"))
            except:
                print("It isn't a number.")
            else:
                number = Number_2()
                number.gongyinshu(num1, num2)

        elif Set == "-i -c mtp":
            try:
                numX = int(input("<"))
                numY = int(input("<"))
            except:

                print("It isn't a number.")
            else:
                number = Number_2()
                number.gongbeishu(numX, numY)

        elif Set == "-p -J Ring":
            try:
                num1 = int(input("number -- "))
                num2 = int(input("Start with a few -- "))
                num3 = int(input("Start with the number few -- "))
                num4 = int(input("Every few suicides -- "))
            except:
                print("It isn't a number.")
            else:
                number = Number_2()
                number.yuesefuhuan(num1, num2, num3, num4)

        elif Set == '-i Mersenne' or '-i Mer':
            numX = int(input('<'))
            Mersenne(numX)
            
        else:
            print("Please write a real instruction.")
            
    else:
        number = Number(num)
        number.judge()

        

# end结束动画

name = [" ","n", "u", "m", 'b', "e", "r", "X", " "]
print("Next to meet you.")
print()
for i in range(5):
    time.sleep(0.2)
    print("-", end='')
for i in name:
    time.sleep(0.2)
    print(i, end='')
for i in range(5):
    time.sleep(0.2)
    print("-", end='')
