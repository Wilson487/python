"""
Topic:請使用input and print打造對話機器人
e.g.
old = input("How old are you?")
print("I am " + old)
1.Show:How old are you?
2.input:12
3.Output:I am 12
"""
WW = input('請輸入你的智商')
print('你這個大傻逼，居然只有' + WW + '點點智商')
"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""

w = input("請輸入體重:")
h = input("請輸入身高(公尺):")
h = float(h)
W = float(W)
bmi = w / h**2
print("你的BMI為" + bmi)
