
import product

class Inventory:
    def __init__(self, products_file):
        self.products_file = products_file
        self.inventory = Inventory.unpack(self, self.products_file)
        self.inventory_count = len(self.inventory)

    def unpack(self, products_file):
        data = open(products_file).readlines()
        inventory = []
        for d in data:
            current = d.rstrip("\n").split(",")

            # Constructor argments
            name = current[0]
            description = current[1]
            value = int(current[2])
            quantity = int(current[3])

            p = product.Product(name, description, value, quantity)
            inventory.append(p)
        return inventory

    def get_inventory(self):
        return self.inventory

    def get_inventory_count(self):
        return self.inventory_count

    def print_inventory(self):
        result = ""
        for each in self.inventory:
            result += str(each)
        # print(result)
        return result

    def get_inventory_value(self):
        total = 0
        for each in self.inventory:
            total += (each.get_value() * each.get_quantity())
        return total

    def __str__(self):
        count = "This inventory has %d items." % self.inventory_count
        value = "It has a total value of (%d)." % self.get_inventory_value()
        inventory = "It has the following items: %s" % self.print_inventory()
        return "%s\n%s\n%s" % (count, value, inventory)

inv = Inventory("./products.txt")
print(str(inv))
