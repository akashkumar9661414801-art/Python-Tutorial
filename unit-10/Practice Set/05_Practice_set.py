class Order:
    def __init__(self,items,Price):
        self.items=items
        self.Price=Price
    def __gt__(self,order2):
        return self.Price>order2.Price
        
    
order1=Order("amrud",20)
order2=Order("tea",15)

print(order1>order2)

