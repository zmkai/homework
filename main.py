from driver import Driver
from car import Car
from depot import Depot
from stopposition import Stopposition
import random
from order import Order
from stop_record import StopRecord as Stop_record
import time

mycar1 = Car('兰博基尼1','红色','11111','小型车','蓝色','辽A11111')
mycar2 = Car('兰博基尼2','红色','22222','小型车','红色','辽A22222')
mycar3 = Car('兰博基尼3','红色','33333','小型车','黑色','辽A33333')
mycar4 = Car('兰博基尼4','红色','44444','小型车','白色','辽A44444')
mycar5 = Car('兰博基尼5','红色','55555','小型车','黄色','辽A55555')
mycars = [mycar1,mycar4]

driver1 =  Driver('小明',18,mycars,'123414','12345123436')
driver2 =  Driver('小红',18,mycars,'123415','12345123437')
drivers = [driver1,driver2]
# 0代表空闲
stopposition1 = Stopposition('1',0.5,'0')
stopposition2 = Stopposition('2',0.5,'0')
stopposition3 = Stopposition('3',0.5,'0')

stoppositions = [stopposition1,stopposition2,stopposition3]
depot1 = Depot(stoppositions,'浑河新区世纪新城','新城停车场',3,'小型车',3)
depot2 = Depot(stoppositions,'浑河新区世纪新城1','新城停车场1',3,'小型车',3)

index = random.randint(0,1)
driver = drivers[index]

driver.drive_car()
driver.come_in_depot(depot2)

stop_order = Stop_record('1',driver.cars[0].car_id,time.time())
# depot2.produce_record()
# stop_order.set_come_time = time.time()

driver.stop_on_position(stopposition1,time.time(),stop_order)
# depot2.update_record()
# stop_order.set_stop_time(time.time())
driver.leaf_position(stop_order,time.time(),stopposition1)
# stop_order.set_leave_time(time.time())
driver.arriver_export()

order = Order('1',50,'支付宝','未支付'," "," ",stop_order.id,"未完成")
# print(order.__dict__)
depot2.produce_order_record(stop_order,order)
driver.pub_free(order)
driver.leave_depot(time.time(),stop_order,depot2)
# stop_order.set_out_time(time.time)






