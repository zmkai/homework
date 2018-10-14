from driver import Driver
from car import Car
from depot import Depot
from stopposition import Stopposition

mycar = Car('跑车','红色')
driver =  Driver('小明',22,mycar)
driver.drive_car()
driver.come_in_depot()
stopposition = Stopposition(10,20,5,'0')
stopposition1 = Stopposition(10,20,0.5,'0')
stoppositions = [stopposition,stopposition1]
depot = Depot(stoppositions,2)
depot.produce_record()
driver.drive_car()
driver.stop_on_position()
depot.update_record()
driver.stop_car()
driver.go_shopping()
driver.go_eation()
driver.leaf_position()
depot.update_record()
driver.arriver_depot()
depot.produce_order_record()
driver.pub_free()
driver.leave_depot()



