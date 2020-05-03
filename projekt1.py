import csv
import sys

items = [{'name':'sugar', 'quantity': 250, 'unit': 'kg', 'unit_price': 1.50},
         {'name': 'juice', 'quantity': 180, 'unit': 'ml', 'unit_price': 5.50},
         {'name':'flour', 'quantity': 320, 'unit': 'kg', 'unit_price': 0.80}]
sold_items = list()


def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    for product in items:
        print(product['name'],"\t",product['quantity'],"\t","\t",product['unit'],"\t","\t", product['unit_price'])

def add_item(name:str,quantity:int,unit:str,unit_price:float):
    new_item = {'name': name,'quantity': quantity,'unit': unit,'unit_price':unit_price}
    items.append(new_item)

def sell_item(to_sell:str, chosen_quantity:int):
    exists = bool()

    for product in items:
        exists = product['name'] == to_sell
        if exists:
            break


    if exists:
         for product in items:
            if product['name']== to_sell:
                product['quantity'] = int(product['quantity'])-chosen_quantity
                sell_info ={'name': to_sell, 'quantity': chosen_quantity, 'unit':product['unit'], 'unit_price':product['unit_price']}
                sold_items.append(sell_info)

    else:
        print('Product not exists')

    return exists

def get_cost():
    sum_costs = float()
    for product in items:
        sum_costs += float(product['quantity']) * float(product['unit_price'])
    return sum_costs

def get_income():
    sum_income = float()
    for product in sold_items:
        sum_income +=  float(product['quantity']) * float(product['unit_price'])
    return sum_income

def show_revenue():
    revenue = get_income() - get_cost()
    print(f"""Revenue breakdown(PLN)
Income: {get_income():.2f}
Costs: {get_cost():.2f}
---------------------
Revenue: {revenue:.2f} PLN
""")

def export_to_csv():
    with open('magazyn.csv','w', newline='') as csvfile:
        fieldnames = ['name','quantity','unit','unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in items:
            writer.writerow({'name': product['name'], 'quantity': product['quantity'], 'unit': product['unit'], 'unit_price': product['unit_price']})
    csvfile.close()

def export_sales_to_csv():
    with open('sales.csv','w',newline='') as csvfile:
        fieldnames = ['name','quantity','unit','unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in sold_items:
            writer.writerow({'name': product['name'], 'quantity': product['quantity'], 'unit': product['unit'], 'unit_price': product['unit_price']})
    csvfile.close()

def load_items_from_cvs():
    if len(sys.argv)>1:
        parametr = sys.argv[1]
    else:
        parametr = 'magazyn.csv'

    items.clear()
    with open(parametr,'r',newline='') as csvfile:
        read = csv.DictReader(csvfile)
        for row in read:
            items.append(row)
    csvfile.close()


def main():
    if len(sys.argv)>1:
        load_items_from_cvs()
        print('Successfully loaded data')

    while True:
        decision = input('What would you like to do? ')
        if decision == 'show':
            get_items()
        elif decision == 'exit':
            print('Exiting.... bye!')
            break
        elif decision == "add":
            print("Adding to warehouse...")
            new_product_name = input("Product name: ")
            new_product_quantity = int(input("Quantity: "))
            new_product_unit = input("Unit of measure: ")
            new_product_unit_price = float(input("Unit price in PLN: "))
            add_item(new_product_name,new_product_quantity,new_product_unit,new_product_unit_price)
            print("Successfully added to warehouse.Current status:")
            get_items()
        elif decision == 'sell':
            chosen_item = input("Item name: ").lower()
            chosen_quantity = int(input("Quantity: "))

            sell_function= sell_item(chosen_item,chosen_quantity)
            if sell_function:
                print(f'Successfully sold {chosen_quantity} of {chosen_item}')
                get_items()
        elif decision == 'show_revenue':
            show_revenue()
        elif decision == 'save':
            export_to_csv()
            export_sales_to_csv()
            print('Successfully exported data to magazyn.csv')
        elif decision == 'load':
            load_items_from_cvs()
        else:
            print("There's no option like this")





if __name__ == '__main__':
   main()

