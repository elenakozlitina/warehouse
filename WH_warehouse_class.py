class WareHouse ():

    def __init__(self, label:str, warehouse_capacity: float ):
        self.label = label
        self.capacity = warehouse_capacity
        self.stock = {} # save material + quantity
    def __str__(self):
        return f'Sklad "{self.label}" with capacity of {self.capacity}'
    def update_label (self, new_label):
        self.label = new_label 
        return f"New label is {new_label}"
    def update_capacity(self, new_capacity :float):
        self.capacity = new_capacity
        return f'New capacity of {self.label} is {self.capacity}'
    def clear (self):
        self.label = ''
        self.capacity = 0
        return f"WareHouse is cleared"
    
    def add_materials(self, material, quantity):
        if material.label in self.stock:
            self.stock[material.label]+= quantity
        else:
            self.stock[material.label] = quantity
        
        if self.get_total_stock() > self.capacity:
            raise ValueError (f' There is no SO MUCH space on {self.label}')
    
    def remove_materials (self, material, quantity):
        if material.label in self.stock and self.stock[material.label]>= quantity :
            self.stock[material.label] -= quantity
            if self.stock[material.label] == 0:
                del self.stock[material.label]
        else:
            raise ValueError('There are no enough {material.label} at {self.label}')
    def get_total_stock(self):
        return sum(self.stock.values())      


