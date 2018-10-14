from stopposition import Stopposition
class Depot():
    def __init__(self,stoppositions,number):
        self.stoppositions = stoppositions
        self.number = number
    
    def produce_record(self):
        print('产生停车记录')
    
    def update_record(self):
        print('修改停车记录')

    def produce_order_record(self):
        print('系统根据停车时间生成订单')