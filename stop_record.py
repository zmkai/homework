from car import Car
class StopRecord():
# 进入停车场的时间
# 停到车位的时间
# 记录编号
# 车牌号
# 停车场（哪个停车场）
# 离开车位时间
# 离开停车场的时间
    # def __init__(self,come_time,stop_time,id,car_id,depot_id,leave_time,out_time):
    #     self.come_time = come_time
    #     self.stop_time = stop_time
    #     self.id = id
    #     self.car_id = car_id
    #     self.depot_id = depot_id
    #     self.leave_time = leave_time
    #     self.out_time = out_time
    def __init__(self,id,car_id,come_time):
        self.id = id
        self.car_id = car_id
        self.come_time = come_time

    def set_come_time(self,come_time):
        self.come_time = come_time
    def set_stop_time(self,stop_time):
        self.stop_time = stop_time
    def set_leave_time(self,leave_time):
        self.leave_time = leave_time

    def set_out_time(self,out_time):
        self.out_time = out_time