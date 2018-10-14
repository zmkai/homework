from  car import Car
class Driver():
    def __init__(self,name,age,mycar):
        self.name = name
        self.age = age
        self.car = mycar
    def drive_car(self):
        print('车主开车')

    def stop_car(self):
        print('车主停车')
    
    def pub_free(self):
        print('车主缴费')
    
    def stop_on_position(self):
        print('车主停车到车位')

    def leaf_position(self):
        print('车主驶出车位')

    def come_in_depot(self):
        print('进入停车场')

    def leave_depot(self):
        print('离开停车场')

    def go_shopping(self):
        print('去购物')

    def go_eation(self):
        print('去吃饭')

    def arriver_depot(self):
        print('到达出口')
    def do_something(self):
        print('做其他事')