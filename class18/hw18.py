'''
有一組字典裡面包含了大家的成績，請列印出來大家的姓名與成績
book = {"小名":"80","大王":"75","事騎":"89","輪輪":"90","柏翰":"68","與誠":"87"}
列印出
小名拿到80分
大王拿到75分
事騎拿到89分
輪輪拿到90分
柏翰拿到100分
與誠拿到87分
'''
B = {"小名": "80", "大王": "75", "事騎": "89", "輪輪": "90", "柏翰": "100", "與誠": "87"}
for W in B.keys():
    print(W + "是" + B[W] + "分")