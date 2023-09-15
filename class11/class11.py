#使用者輸入一個數字 A
#計算由 0+1+...+ A 的總和,並將總和顯示出來
# A = int(input("請輸入一個整數:"))
# S = 0
# for i in range(A + 1):
#     S = S + i
# S = str(S)
# A = str(A)
# print("從0加到" + A + "的總和為" + S)
A = 1
for i in range(1, 10):
    for j in range(1, 10):
        i = int(i)
        S = j * i
        i = str(i)
        j = str(j)
        S = str(S)
        print(j + "*" + i + "=" + S)
