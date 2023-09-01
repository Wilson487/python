# import turtle

# turtle.color('blue')  #設定小烏龜顏色
# turtle.shape(
#     'turtle')  #設定小烏龜型'arrow','turtle','circle','square','triangle','classic'.
# turtle.stamp()  #蓋章
# turtle.penup()  #提筆
# turtle.done()
import turtle

# turtle.penup()
# turtle.shape('turtle')
# for step in range(5, 61, 2):  #迴圈:從5開始，每次跳兩步，直到60
#     turtle.stamp()  #蓋章
#     turtle.forward(step)  #向前step 步
#     turtle.right(25)
#     print(step)
# turtle.done()
#星形中心為正五邊形，每一外角360度/5=72度
#星形每隻銳角的角度=180度-2*72=36度
turtle.pensize(5)  #線徑寬度1~10
turtle.pencolor("yellow")  #線的顏色
turtle.fillcolor("yellow")  #區域填滿顏色
turtle.begin_fill()  #填滿區域設定開始
for i in range(5):
    turtle.forward(200)
    turtle.right(144)

turtle.end_fill()  #填滿區域設定結束
turtle.done()