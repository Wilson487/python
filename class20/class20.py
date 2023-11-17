# # #鍵檢查
# # A={1:"a",2:"b"}
# # 1 in A
# # print('a' in A)  # True
# # print('A' in A)  # Faise


# # F= { "蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# # A=input("輸入你要檢查食物")
# # if A== "蛋糕":
# #     print("1")
# # elif A == "三明治":
# #     print("10")
# # elif A == "果汁":
# #     print("20")
# # elif A == "薯條":
# #     print("15")
# # elif A == "披薩":
# #     print("2")
# # else:
# #     print("你在無中生有")




# # F= { "蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}

# # F["冰淇淋"]=10
# # F["熱狗"]=20
# # F["果汁"]=25

# # FB= { "蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}

# # for F,count in F.items():
# #     if F == "果汁" :
# #         print(F+str(count)+"杯")
# #     else:
# #         print( F + "是" + str(count) + "份")
# # print("你要買甚麼")
# # for F,count in F.items():
# #     if not (F in FB):
# #         print( F + "是" + str(count) )
# #     elif F in FB and FB[F]:
# #         print(F+str(count FB[F]))


# # #pop 方法
# # B = {1:"a",2:"b"}
# # V= B.pop(1)#把Key移除
# # print(B)
# # print(V)

# # #pop 方法2
# # B = {1:"a",2:"b"}
# # V= B.pop(0,"哈哈你是智能XX")#如果Key不存在,會失敗
# # print(B)
# # print(V)


# # food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# # food_list["冰淇淋"] = 10
# # food_list["熱狗"] = 20
# # food_list["果汁"] = 25
# # # 派對後剩下的食物和數量
# # remaining_food = {"蛋糕": 0, "三明治": 5, "果汁": 8, "薯條": 10, \
# #                 "披薩": 1, "冰淇淋": 3, "熱狗": 0}
# # # 更新食物列表並移除已經吃完的食物
# # for food, count in remaining_food.items():
# #     if count == 0:
# #         food_list.pop(food, None)
# #         print(food + "已經吃完")
# #     else:
# #         food_list[food] = count
# # for food, count in food_list.items():
# #     if food == "果汁":
# #         print(food + ": " + str(count) + "杯")
# #     else:
# #         print(food + ": " + str(count) + "份")

# food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# print(len(food_list)) #算Key的數量
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25
# print(len(food_list))

T={"明":"樂高","花":"筆","強":"球","美":"書","偉":"遙控車"}
A=str(len(T))
print("有"+A+"個禮物")
for W in T.keys():
    
    print("小"+W+ "是" + T[W] )
