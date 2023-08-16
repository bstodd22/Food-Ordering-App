class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FoodOrder:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

def display_menu(menu):
    print("Menu:")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item.name} - ${item.price:.2f}")

def main():
    menu = [
        FoodItem("Burger", 5.99),
        FoodItem("Pizza", 8.99),
        FoodItem("Salad", 4.49),
        FoodItem("Fries", 2.99)
    ]

    order = FoodOrder()

    while True:
        display_menu(menu)
        choice = int(input("Enter the item number you want to order (0 to finish): "))
        
        if choice == 0:
            break

        if 1 <= choice <= len(menu):
            chosen_item = menu[choice - 1]
            order.add_item(chosen_item)
            print(f"{chosen_item.name} added to your order.")
        else:
            print("Invalid choice. Please select a valid item number.")

    total = order.calculate_total()
    print(f"Your order total: ${total:.2f}")
    print("Thank you for ordering!")

if __name__ == "__main__":
    main()