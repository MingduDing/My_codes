# -*- coding: utf-8 -*-
cars = 100  # 100辆车
space_in_a_car = 4.0  # 每辆车可以坐4个人
drivers = 30  # 司机30人
passengers = 90  # 乘客90人
cars_not_driven = cars - drivers  # 无用车辆
cars_driven = drivers  # 可用车辆
carpool_capacity  = cars_driven * space_in_a_car  # 总的车辆运载能力
average_passengers_per_car = passengers / cars_driven  # 平均每辆车需要坐多少乘客

print "There are", cars, "cars avaliable."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"