from stopposition import Stopposition
from order import Order
class Depot():
    def __init__(self,stoppositions,address,name,stopposition_count,position_type,free_count):
        self.stoppositions = stoppositions
        self.address = address
        self.name = name
        self.stopposition_count = stopposition_count
        self.position_type = position_type
        self.free_count = free_count
    
    def produce_record(self):
        print('产生停车记录')
    
    def update_record(self):
        print('修改停车记录')

    def produce_order_record(self,stop_record,order):
        print('系统根据停车时间生成订单')
        print('依据的停车记录id'+stop_record.id)
        print('生成的订单号为'+order.order_id)
