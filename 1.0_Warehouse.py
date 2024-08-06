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




class Material ():
    def __init__(self, label: str,unit: str, unit_price: float, quantity:float ):
        self.label = label 
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity
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





class InventoryManagement ():
    def __init__(self):
        self.warehouses = {}
    def add_warehouse(self, warehouse):
        self.warehouses[warehouse.label] = warehouse
    def transfer_material (self, material, quantity, from_warehouse, to_warehouse):
        if from_warehouse not in self.warehouses or to_warehouse not in self.warehouses:
            raise ValueError ("There is no at least one of these warehuses")
        source_warehouse = self.warehouses[from_warehouse]
        target_warehouse = self.warehouses[to_warehouse]

        source_warehouse.remove_materials(material, quantity)
        try:
            target_warehouse.add_materials(material, quantity)
        except ValueError:
            source_warehouse.add_materials(material, quantity)
            raise





General_Warehouse = WareHouse("General", 20000)
Factory_Warehouse = WareHouse("Factory", 1000)
#нужно сделать как-то так чтобы при добавлении материала он автоматически заносился на обычный склад
# потому что так есть возможность потерять его как мы умудрились уже 
coffee = Material("coffee", unit = "kg", unit_price = 200, quantity= 300)
pack_0_25 = Material("pack 0.25", unit = "pc", unit_price=3, quantity = 200)

inventory = InventoryManagement()
inventory.add_warehouse(General_Warehouse)
inventory.add_warehouse(Factory_Warehouse)

General_Warehouse.add_materials(coffee, 120)
General_Warehouse.add_materials(pack_0_25, 20)
Factory_Warehouse.add_materials(coffee, 120)
Factory_Warehouse.add_materials(pack_0_25, 50)

inventory.transfer_material(pack_0_25, 10, "General", "Factory")

print("Sklad 1 zapasy :", General_Warehouse.stock)
print("Sklad 2 zapasy :", Factory_Warehouse.stock)


