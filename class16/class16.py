# A = ["a", "b", "c"]
# print(A)
# A[0] = "I"
# print(A)
# A = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
# print(A)
# input("輸入要改的星期數字")
# A[5] = "晴天"
# print(A)
'''
while True:
    print("晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天")
    A = str(input("輸入要改的星期數字:"))
    a = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
    if A == "1":
        print("你要改的星期數是星期1")
        print("原本天氣是晴天")
        B = str(input("輸入要改的天氣:"))
        print(B + "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天")
    elif A == "2":
        print("你要改的星期數是星期2")
        print("原本天氣是多雲")
        C = str(input("輸入要改的天氣:"))
        print("晴天" + C + "雨天", "晴天", "多雲", "雷陣雨", "晴天")
    elif A == "3":
        print("你要改的星期數是星期3")
        print("原本天氣是多雲")
        D = str(input("輸入要改的天氣:"))
        print("晴天", "多雲" + D + "晴天", "多雲", "雷陣雨", "晴天")
    elif A == "4":
        print("你要改的星期數是星期4")
        print("原本天氣是多雲")
        E = str(input("輸入要改的天氣:"))
        print("晴天", "多雲", "雨天" + E + "多雲", "雷陣雨", "晴天")
    elif A == "5":
        print("你要改的星期數是星期5")
        print("原本天氣是多雲")
        F = str(input("輸入要改的天氣:"))
        print("晴天", "多雲", "雨天", "晴天" + F + "雷陣雨", "晴天")
    elif A == "6":
        print("你要改的星期數是星期6")
        print("原本天氣是多雲")
        G = str(input("輸入要改的天氣:"))
        print("晴天", "多雲", "雨天", "晴天", "多雲" + G + "晴天")
    elif A == "7":
        print("你要改的星期數是星期7")
        print("原本天氣是多雲")
        H = str(input("輸入要改的天氣:"))
        print("晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨" + H)
    else:
        print("輸入錯誤查無此天氣，重新輸入吧!你這個傻逼!")
'''

# A = ["a", "b", "c"]
# a = A.copy()
# a[0] = 1
# print(A, a)

# A_list = [
#     "火龍果",
#     "哈密瓜",
#     "百香果",
#     "橘子",
#     "蘋果",
#     "香蕉",
#     "梨",
#     "李",
#     "桃",
# ]
# print("最長的名子是" + max(A_list))
# print("最短的名子是" + min(A_list))

B = "2023/10/20"
B = B.split("/")
B = "-".join(B)
print(B)