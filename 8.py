import turtle
turtle.speed(100)
turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(180)
turtle.pendown()

#ручка
turtle.color('#4169E1')
turtle.width(10)
turtle.forward(35)
turtle.right(70)
turtle.forward(120)
turtle.left(180)
turtle.forward(90)
turtle.right(110)

#корзина
turtle.forward(240)
turtle.right(110)
turtle.forward(110)
turtle.right(70)
turtle.forward(165)

#низ
turtle.left(110)
turtle.forward(30)
turtle.left(70)
turtle.forward(150)

turtle.penup()
turtle.left(70)
turtle.forward(140)
turtle.left(110)
turtle.forward(122)
turtle.pendown()

#решеткаверт
turtle.color('#D0C4DE')
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.forward(41)
turtle.left(80)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.left(180)
turtle.forward(100)
turtle.right(80)
turtle.forward(82)
turtle.pendown()
turtle.right(80)
turtle.forward(100)

#решеткагоризонт
turtle.penup()
turtle.left(80)
turtle.forward(65)
turtle.left(110)
turtle.forward(30)
turtle.left(70)
turtle.pendown()
turtle.forward(215)
turtle.penup()
turtle.right(110)
turtle.forward(35)
turtle.right(70)
turtle.pendown()
turtle.forward(190)

#границы
turtle.penup()
turtle.left(110)
turtle.forward(20)
turtle.pendown()
turtle.color('#4169E1')
turtle.left(180)
turtle.forward(87)
turtle.right(110)

#корзина
turtle.forward(240)
turtle.right(110)
turtle.forward(110)
turtle.right(70)
turtle.forward(165)

#колеса
turtle.penup()
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(30)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.done()
