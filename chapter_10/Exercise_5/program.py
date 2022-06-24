import retailitem

item1 = retailitem.RetailItem('Jacket', 12, 59.95)
item2 = retailitem.RetailItem('Designer Jeans', 40, 34.95)
item3 = retailitem.RetailItem('Shirt', 20, 24.95)
item_list = []
item_list.append(item1)
item_list.append(item2)
item_list.append(item3)

print()
print('\t\tDescription\t\tUnits in Inventory\tPrice')
print('-------------------------------------------------------------------------------')
print(f'Item #1\t\t{item1.get_description()}\t\t\t{item1.get_units()}\t\t\t{item1.get_price()}')
print(f'Item #2\t\t{item2.get_description()}\t\t{item2.get_units()}\t\t\t{item2.get_price()}')
print(f'Item #3\t\t{item3.get_description()}\t\t\t{item3.get_units()}\t\t\t{item3.get_price()}')
print('-------------------------------------------------------------------------------')
