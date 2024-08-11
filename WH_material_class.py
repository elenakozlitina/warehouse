

class Material ():
    def __init__(self, label: str,unit: str, unit_price: float, quantity:float, warehouse :str):
        self.label = label 
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity
        self.add_to_warehouse(warehouse, quantity)

    def add_to_warehouse(self, warehouse, quantity):
        if warehouse.capacity >= self.quantity:
            warehouse.add_materials(self, quantity)
            print(f'Material {self.label} added to warehouse {warehouse.label} ({self.quantity})')
        else:
            raise ValueError(f'Not enough capacity in warehouse {warehouse.label} for material {self.label}.')

    def __str__(self) -> str:
        return f"Material lable : {self.label}, raw_price : {self.raw_price}"
    def update_label (self, new_label: str):
        self.label = new_label
        return f"The lable of the material is {self.label} now"
    def update_raw_price (self, new_raw_price :float):
        self.raw_price = new_raw_price 
        return f'New raw price for {self.label} is {self.raw_price}'
    def clear (self):
        self.label = ''
        self.raw_price = 0
        return f'The material is kinda cleard but you still can find it with no lable or raw_price'



