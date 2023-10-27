'''
請幫點餐機設計一個選單，當顧客
使用點餐機時，可以看到所有可以
選擇的功能，並告訴機器他們想做什麼。
歡迎使用點餐機！請選擇您想要的功能(輸入數字)：
1. 新增餐點到點餐清單
2. 從點餐清單中移除特定餐點
3. 在指定位置加入餐點
4. 計算點餐清單中某餐點的數量
5. 取消點餐清單中的最後一項餐點
6. 取消點餐清單中特定位置的餐點
7. 顯示升序排序的點餐清單
8. 顯示降序排序的點餐清單
9. 反轉點餐清單的順序
10. 查詢餐點在點餐清單中的位置
11. 退出點餐機
'''
A_list = []
while True:
    print("歡迎使用點餐機！請選擇您想要的功能(輸入數字)")
    print("1. 新增餐點到點餐清單")
    print("2. 從點餐清單中移除特定餐點")
    print("3. 在指定位置加入餐點")
    print("4. 退出點餐機")
    A = input("輸入要改的功能數字:")
    if A == "1":
        print("你選了新增餐點到點餐清單的功能")
        new_list = input("輸入新的菜單")
        A_list.append(new_list)
        print("OK")
    elif A == "2":
        order = input("輸入你要移除的餐點")
        if order in A_list:
            A_list.remove(order)
            print("OK")
        else:
            print("你在無中生有")
    elif A == "3":
        P = int(input("輸入你要插入的位置"))
        order = input("輸入你要插入的餐點")
        A_list.insert(P, order)
        print("OK")
    elif A == "4":
        order = input("輸入你要計算的餐點")
        C = A_list.count(order)
        print("餐點" + order + "數量是" + str(C))
    elif A == "5":
        if A_list:
            A_list.pop()
            print("OK")
        else:
            print("你在無中生有")
    elif A == "6":
        P = int(input("輸輸入位置"))
        if 0 <= P < len(A_list):
            A_list.pop(P)
            print("OK")
        else:
            print("你在無中生有")
