from  car import Car
from depot import Depot
from stopposition import Stopposition
from order import Order
from stop_record import StopRecord as Stop_record
class Driver():
    def __init__(self,name,age,mycars,id,telephone):
        self.name = name
        self.age = age
        self.cars = mycars
        self.id = id
        self.telephone = telephone
        
    def drive_car(self):
        print(self.name+'开车'+self.cars[0].car_name)

    def stop_car(self):
        print('车主停车')
    
    def pub_free(self,order):
        print('车主根据订单'+order.order_id+'缴费')
    
    def stop_on_position(self,stop_position,stop_time,stop_order):
        stop_order.stop_time = stop_time
        print('车主在'+str(stop_time) +'时刻停车到'+stop_position.id+'车位')


    def leaf_position(self,stop_order,leave_time,stopposition):
        stop_order.leave_time = leave_time
        print('车主'+str(leave_time)+'时刻驶出'+stopposition.id+'车位')
        print('停车记录已经修改')

    def come_in_depot(self,depot1):
        print(self.name+'进入'+depot1.name+'停车场')

    def leave_depot(self,out_time,stop_order,depot):
        stop_order.out_time = out_time
        print(self.name+'开车离开'+depot.name+'停车场')
        print(self.name+'车主离开停车场时间已记录')

    def go_shopping(self):
        print('去购物')

    def go_eation(self):
        print('去吃饭')

    def arriver_export(self):
        print(self.name+'开车到达出口')
    def do_something(self):
        print('做其他事')