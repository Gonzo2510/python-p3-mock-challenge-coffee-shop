#!/usr/bin/env python3
# import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

# if __name__ == '__main__':
#     print("HELLO! :) let's debug")
    # ipdb.set_trace()

# coffee_1 = Coffee("latte")
# coffee_2 = Coffee("mocha")
# coffee_3 = Coffee("ice coffee")

# customer_1 = Customer("Steve")
# customer_2 = Customer("Jacob")
# customer_3 = Customer("Isabel")


# order_1 = Order(customer_1, coffee_1, 2.0)
# order_2 = Order(customer_1, coffee_1, 5.0)
# # order_3 = Order(customer_1, coffee_2, 5.0)
# order_4 = Order(customer_2, coffee_1, 3.0)
# order_5 = Order(customer_2, coffee_1, 3.0)
# order_6 = Order(customer_3, coffee_1, 3.0)


coffee = Coffee("Vanilla Latte")
customer = Customer("Steve")
customer_2 = Customer("Dima")
Order(customer, coffee, 2.0)
Order(customer_2, coffee, 2.0)
Order(customer, coffee, 5.0)

print()

coffee.customers()
x= len(set(coffee.customers()))
y = len(coffee.customers())

print(x, y)