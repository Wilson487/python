'''
今天python一樣要做自我介紹，他要介紹自己的年齡，班上有一位同學她今年8歲，你們要讓python說出自己跟那位同學加起來幾歲！
EX:
請輸入python年齡:10
python與同學年齡加起來16歲
'''
同學 = 8
python = input("請輸入python年齡")
python = int(python)
兩者年齡 = 同學 + python
print("python與同學年齡加起來%d歲" % (兩者年齡))
