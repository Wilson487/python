# append
I = [1, 2, 3]
I.append(4)  #加4到裡面
print(I)

#remove
I = ["a", "b", "c", "a"]
I.remove("a")  #把I.remove裡的東東移除,移除第一個出現的東東
print(I)

#insert
I = [1, 2, 3]
I.insert(1, "b")  #在指定位置插入東東
print(I)

#count
I = [9, 1, -4, 3, 7, 11, 3]
print(I.count(3))  #算特定元素的數量

#pop
I = [1, 2, 3]
I.pop(0)  #把元素移除
print(I)