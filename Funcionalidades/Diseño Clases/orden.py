
class Order:
    count_order = 0

    def __init__(self):

        Order.count_order += 1
        self.__id_order = Order.count_order
        self.product_list = []

    def add_product(self, product):

        self.product_list.append(product)        
    
    def calc_total(self):

        total = 0
        for i in range(len(self.product_list)):
            total += self.product_list[i].price

        return total 
    
    def get_products(self):
        
        return self.product_list
        
    
        







