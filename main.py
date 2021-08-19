import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# TODO: 1.创建玩家小乌龟（继承turtle),实现玩家响应上键移动
player = Player()
car_manager = CarManager()
# TODO: 2.1 创建scoreboard类，显示等级
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # TODO: 2.创建车类，（继承turtle)，实现自左向右的移动

    # # TODO: 3.随机使得车对象的位置随机生成（Y），生成时间要间隔一定时间，每次生成数量，放置玩家没法玩。
    car_manager.move()
    # TODO: 5.如果未碰撞，且玩家的X坐标超出预定值，重新设置玩家位置，并将level提升
    if player.ycor() > 280:
        player.go_back()
        scoreboard.game_up()
        car_manager.accelerate()
    # TODO: 4.检测玩家与车辆的碰撞信息（所有）？列表处理？

    for car in car_manager.car_list:
        if abs(player.xcor() - car.xcor()) < 28 and abs(player.ycor() - car.ycor()) < 18:
            scoreboard.failed()
            game_is_on = False

    screen.update()

screen.exitonclick()
