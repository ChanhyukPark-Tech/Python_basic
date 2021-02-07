 
 
class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
         print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))


class H1(House):
    def __init__(self):
        super().__init__("GangNam","Apart","Forever","10billion","2010 year")


H1 = H1()
H1.show_detail()
