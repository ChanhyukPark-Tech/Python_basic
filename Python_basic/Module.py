# import theater_module 
# theater_module.price(3) # 3people go to theater
# theater_module.price_morning(4) 
# theater_module.price_soldier(5) # 5 people soldier go to movie

import theater_module as mv #nickname
mv.price(3)
#....as.as..a.as.a.s as mv

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price,price_morning # im not soldier !


from theater_module import price_soldier as price
price(5) # <=====soldier !!!! caution!
