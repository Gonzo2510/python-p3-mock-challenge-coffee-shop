#!/usr/bin/env python3
# import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    # ipdb.set_trace()
print()

coffee1 = Coffee("latte")
coffee2 = Coffee("mocha")
coffee3 = Coffee("ice coffee")

customer = Customer("Steve")

order_1 = Order(customer, coffee_1, 2.0)
order_2 = Order(customer, coffee_1, 5.0)
order_3 = Order(customer, coffee_2, 5.0)





print()