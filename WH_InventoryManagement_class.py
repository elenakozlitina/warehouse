
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



