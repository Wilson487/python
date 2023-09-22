#從一顯示到六，跳過三
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# A = int(input("請輸入跳繩次數:"))
# for i in range(1, A + 1):
#     if i % 10 == 0:
#         print("我跌倒了")
#         continue
#     print("第" + str(i) + "跳繩")

# import random

# random.randrange(3)
# random.randrange(0, 10000000, 2)不能抽到結尾!
# print(random.randrange(3))
# print(random.randrange(0, 10, 2))

# print(random.randint(1, 3))#能抽到結尾
# print(random.randint(1, 10))

# import random as r  #把random改名成r

# print(r.randint(1, 10))
# print(r.randrange(1, 10))

# import random as r

# A = r.randrange(0, 101)
# S = -1
# while S != A:
#     S = int(input("輸入1到100的整數:"))
#     if S > A:
#         print("再小一點")
#     elif S < A:
#         print("再大一點")
# print("算你幸運")