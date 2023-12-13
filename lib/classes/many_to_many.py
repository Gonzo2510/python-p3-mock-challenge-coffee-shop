class Coffee:

    def __init__(self, name):
        self._name = name

    # def __repr__(self) -> str:
    #     return f'Coffee: {self.name}'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
        
    def orders(self):
        # orders = []
        # for order in Order.all:
        #     if order.coffee.name == self.name:
        #         orders.append(order)
        # print(orders)
        # return orders

        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        # customers = []
        # for order in Order.all:
        #     if order.coffee.name == self.name:
        #         if order.customer not in customers:
        #             customers.append(order.customer)
        # return customers

        return list({order.customer for order in Order.all if order.coffee is self})
    
    def num_orders(self):
        return len(self.orders())

    
    def average_price(self):
        if len(self.orders()) > 0:
            total = 0
            for order in self.orders():
                total += order.price
            return total / len(self.orders())
        return 0








class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 15):
            self._name = name    
        
    def orders(self):
        # return list(order.coffee for order in Order.all if order.customer == self)

        orders = []
        for order in Order.all:
            if order.customer == self:
                orders.append(order)
        return orders
    
    def coffees(self):
        coffees = []
        for order in Order.all:
            if order.customer == self:
                if order.coffee not in coffees:
                    coffees.append(order.coffee)
        return coffees
    
    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee) and type(price) == float:
            order = Order(self, coffee, price)
        return order




class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    def __repr__(self) -> str:
        return self.customer, self.coffee, self.price
        

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self, "price"):
            if isinstance(price, float) and 1.0 <= price <= 10.0:
                self._price = price
    