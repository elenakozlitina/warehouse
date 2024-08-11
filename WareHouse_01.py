from  WH_material_class import Material
from  WH_warehouse_class import WareHouse
from  WH_InventoryManagement_class import InventoryManagement

General_Warehouse = WareHouse("General", 20000)
Factory_Warehouse = WareHouse("Factory", 1000)
coffee = Material("coffee", unit = "kg", unit_price = 200, quantity= 300, warehouse= General_Warehouse)
pack_0_25 = Material("pack 0.25", unit = "pc", unit_price=3, quantity = 200, warehouse= Factory_Warehouse)

inventory = InventoryManagement()
inventory.add_warehouse(General_Warehouse)
inventory.add_warehouse(Factory_Warehouse)

#inventory.transfer_material(pack_0_25, 10, "General", "Factory")

print("General warehouse zapasy :", General_Warehouse.stock)
print("Factory warehouse zapasy :", Factory_Warehouse.stock)



