# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


import csv
inv = {'rope': 1, 'torch': 6, 'gold coin': 142, 'dagger': 1, 'arrow': 12}


# Displays the inventory.
def display_inventory(inventory):
    print ("Inventory:")
    total_number_of_items = 0
    for key, value in inventory.items():
        print (value, key)
        total_number_of_items += value
    print ("Total number of items:", total_number_of_items)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order="count,desc"):
    width = max(len(x)for x in inventory.keys()) + 4
    print ("Inventory:")
    print ("count".rjust(7, " ") + "item name".rjust(width, " "))
    print ("-"*20)
    if order == "count,desc":
        sorted_values = sorted(inventory.values(), reverse=True)
        sorted_keys = sorted(inventory, key=inventory.__getitem__, reverse=True)
    elif order == "count,asc":
        sorted_values = sorted(inventory.values())
        sorted_keys = sorted(inventory, key=inventory.__getitem__)
    iter = 0
    total_number_of_items = 0
    for i in sorted_values:
        print (str(i).rjust(7, " ") + sorted_keys[iter].rjust(width, " "))
        total_number_of_items += i
        iter += 1
    print ("-"*20)
    print ("Total number of items:", total_number_of_items)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=",")
        new_stuff = []
        for row in reader:
            for item in row:
                new_stuff.append(item)
    add_to_inventory(inventory, new_stuff)
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    old_stuffs = []
    for i in inventory.keys():
        for turn in range(inventory[i]):
            old_stuffs.append(i)
    with open(filename, 'w') as file:
        write_out = csv.writer(file)
        write_out.writerow(old_stuffs)
