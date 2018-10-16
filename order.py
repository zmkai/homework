class Order():
# 订单编号
# 订单金额
# 支付方式
# 支付状态
# 支付时间
# 支付人
# 停车记录编号
# 订单状态
    def __init__(self,order_id,order_money,pay_type,pay_status,pay_time,pay_name,stop_record_id,order_status):
        self.order_id = order_id
        self.order_money = order_money
        self.pay_type = pay_type
        self.pay_status = pay_status
        self.pay_time = pay_time
        self.pay_name = pay_name
        self.stop_record_id = stop_record_id
        self.order_status = order_status
