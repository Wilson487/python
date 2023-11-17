# D={1:"a",2:"b"}
# V=D.values()
# for value in V:
#     print(value)


# D={1:"a",2:"b"}
# V=D.items()
# for item in V:
#     print(item)
#     print(item[0],item[1])

# D={1:"a",2:"b"}
# V=D.items()
# for key in V:
#     print(key,value)

# F= { "蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# for W in F.keys():
#     if W == "果汁" :
#         print("果汁"+"20"+"杯")
#     else:
#         str(F)
#         print( W + "是" + str(F[W]) + "份")


# B = {}
# B["書名"]="天堂之門"  
# B["作者"]="岸邊露伴"
# B

F= { "蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}

F["冰淇淋"]=10
F["熱狗"]=20
for W in F.keys():
    if W == "果汁" :
        print("果汁"+"25"+"杯")
    else:
        print( W + "是" + str(F[W]) + "份")

