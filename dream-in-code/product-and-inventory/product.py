
class Product:
    global_id = 0

    def __init__(self, name, description, value):
        self.id = Product.global_id + 1
        Product.global_id += 1
        self.name = name
        self.description = description
        self.value = value

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return "\nID: " + str(self.id) + "\nName: " + self.name + "\nDescription: " \
            + self.description + "\nValue: " + str(self.value) + "\n"
