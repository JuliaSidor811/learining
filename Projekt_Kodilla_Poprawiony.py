import csv
import sys


class Warehouse:
    def __init__(self):
        self.warehouse = list()
        self.sold_items = list()

    def get_items(self):
        print("Name\tQuantity\tUnit\tUnit Price (PLN)")
        for product in self.warehouse:
            print(f"{product.name} \t {product.quantity} \t \t {product.unit} \t \t {product.unit_price}")

    def add_item(self, product: object):
        if product not in self.warehouse:
            self.warehouse.append(product)

    def sell_item(self, chosen_product: str, quantity: int):
        success = bool()
        for product in self.warehouse:
            if product.name == chosen_product:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    product_sell = Product(product.name, quantity, product.unit, product.unit_price)
                    self.sold_items.append(product_sell)
                    print(f'Successfully sold {quantity} of {chosen_product}')
                    success = True

        if success is not True:
            print('Something went wrong')

    def get_costs(self):
        costs = float()
        for product in self.warehouse:
            costs += product.unit_price * product.quantity
        return costs

    def get_income(self):
        income = float()
        for product in self.sold_items:
            income += product.unit_price * product.quantity
        return income

    def show_revenue(self):
        revenue = self.get_income() - self.get_costs()
        print(f"""Revenue breakdown(PLN)
        Income: {self.get_income():.2f}
        Costs: {self.get_costs():.2f}
        ---------------------
        Revenue: {revenue:.2f} PLN
        """)

    def export_to_csv(self):
        with open('warehouse.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'quantity', 'unit', 'unit_price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.warehouse:
                writer.writerow(
                    {'name': str(product.name), 'quantity': int(product.quantity), 'unit': str(product.unit),
                     'unit_price': float(product.unit_price)})
        csvfile.close()
        with open('sales.csv', 'w', newline='') as csvfile2:
            fieldnames = ['name', 'quantity', 'unit', 'unit_price']
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
            for product in self.sold_items:
                writer.writerow(
                    {'name': str(product.name), 'quantity': int(product.quantity), 'unit': str(product.unit),
                     'unit_price': float(product.unit_price)})
        csvfile2.close()

    def load_items_from_cvs(self):

        if len(sys.argv) > 1:
            parameter = sys.argv[1]
        else:
            parameter = 'warehouse.csv'

        self.warehouse.clear()
        with open(parameter, 'r', newline='') as csvfile:
            read = csv.DictReader(csvfile)
            for row in read:
                product = Product(row["name"], int(row["quantity"]), row["unit"], float(row["unit_price"]))
                self.warehouse.append(product)

        csvfile.close()


class Product:
    def __init__(self, name: str, quantity: int, unit: str, unit_price: float):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unit_price = unit_price


def main():
    warehouse = Warehouse()
    product_at_the_beginning = [Product('Milk', 120, 'ml', 2.3),
                                Product('Sugar', 1000, 'kg', 3),
                                Product('Flour', 12000, 'kg', 1.2),
                                Product('Coffe', 25, 'kg', 40)]
    for product in product_at_the_beginning:
        warehouse.add_item(product)

    if len(sys.argv) > 1:
        warehouse.load_items_from_cvs()
        print('Successfully loaded data')

    while True:
        decision = input('What would you like to do? ')
        if decision == 'show':
            warehouse.get_items()
        elif decision == 'exit':
            print('Exiting.... bye!')
            break
        elif decision == "add":
            print("Adding to warehouse...")
            new_product_name = input("Product name: ")
            new_product_quantity = int(input("Quantity: "))
            new_product_unit = input("Unit of measure: ")
            new_product_unit_price = float(input("Unit price in PLN: "))
            new_product = Product(new_product_name, new_product_quantity, new_product_unit, new_product_unit_price)
            warehouse.add_item(new_product)
            print("Successfully added to warehouse.Current status:")
            warehouse.get_items()
        elif decision == 'sell':
            chosen_item = input("Item name: ").capitalize()
            chosen_quantity = int(input("Quantity: "))
            warehouse.sell_item(chosen_item, chosen_quantity)
            warehouse.get_items()
        elif decision == 'revenue':
            warehouse.show_revenue()
        elif decision == 'save':
            warehouse.export_to_csv()
            print('Successfully exported data')
        else:
            print("There's no option like this")


if __name__ == '__main__':
    main()
