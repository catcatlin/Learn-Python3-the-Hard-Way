cars = 100
space_in_a_car = 4.0 # 每辆车的座位数
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # 没开走的车
cars_driven = drivers # 开走的车
carpool_capacity = cars_driven * space_in_a_car #  车座总数
average_passengers_per_car = passengers / cars_driven # 每辆开走的车的乘客数量

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
