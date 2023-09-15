# HW11:
# 輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
# EX：
# 請輸入開始整數:10
# 請輸入結束整數:50
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
x = int(input("請輸入開始整數"))
A = int(input("請輸入結束整數"))
for i in range(x, A + 1):
    ans = False
    for j in range(2, int(i / 2 + 1)):
        if j != 1:
            if i % j == 0:
                ans = True
    if ans == False:
        print(str(i) + '是質數')

# for i in range(3, 100, 3):
#     print(i)

# for i in range(2, 100):
#   i=i % 2
#   if i==1
#
#         i//=2
#         j = str(j)
#         S = str(S)
#         print(j + "*" + i + "=" + S)
# if x == 1:
#     print(f"{x}不是質數")
# else:
#     i = 2
#     while x % i != 0 and i != x:
#         i += 1
#     if i == x:
#         print("yes")
#     else:
#         print("no")
