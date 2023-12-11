class Coffee:

    def __init__(self, name):
        self._name = name

    def __repr__(self) -> str:
        return f'Coffee: {self.name}'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
        
    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass
















class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 15):
            self._name = name    
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    













class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self, price):
            if isinstance(price, float) and 