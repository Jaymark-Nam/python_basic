
'''
import theater_module
theater_module.price(3)
theater_module.price_morning(1)
theater_module.price_soldier(5)
'''

import theater_module as mv     #mv로 별명 바꾸기
mv.price(3)

from theater_module import *
price(3)
price_morning(3)
price_soldier(1)


from theater_module import price_morning, price  #except soldier
price_morning(2)
price(1)

