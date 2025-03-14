    

pizzas = [
    {
        "name": "Pepperoni",
        "sizes": {
            "Small": 8.99,
            "Medium": 12.99,
            "Large": 15.99,
        },
    },
    {
        "name": "Vegetarian",
        "sizes": {
            "Small": 7.99,
            "Medium": 11.99,
            "Large": 14.99,
        },
    },
    {
        "name": "Margherita",
        "sizes": {
            "Small": 7.50,
            "Medium": 11.50,
            "Large": 14.50,
        },
    },
    {
        "name": "Meat Lovers",
        "sizes": {
            "Medium": 16.99,
            "Large": 19.99,
            "Extra Large": 22.99
        }
    },
    {
        "name": "Hawaiian",
        "sizes": {
            "Small": 9.50,
            "Medium": 13.50,
            "Large": 16.50
        }
    }
]

def display_menu():
    print("Hello, welcome to our pizza shop, here is what we have:")
    for pizza in pizzas:
        print(f"\n{pizza['name']}")
        for size, price in pizza["sizes"].items():
            print(f"  {size}: ${price:.2f}")

def order_placement():
    while True:
        order = input("What do you want to buy? ").strip().title()
        for pizza in pizzas:
            if order == pizza['name']:
                return order
        print("We don't have that here, please select from the menu:")
        display_menu()

def get_pizza_size(sizes):
    while True:
        size = input(f"Please select the pizza size {list(sizes.keys())}: ").title()
        if size in sizes:
            return size
        else:
            print("We don't have that size, please select from our displayed sizes.")

def get_quantity():
    while True:
        quantity = input("How many pizzas do you want? ")
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity >= 1:
                return quantity
            else:
                print("Quantity must be greater than zero.")
        else:
            print("Please enter a valid number.")

def main():
    display_menu()
    order = order_placement()
    for pizza in pizzas:
        if pizza["name"] == order:
            size = get_pizza_size(pizza["sizes"])
            quantity = get_quantity()
            price = pizza["sizes"][size]
            total_price = price * quantity
            print(f"You ordered {quantity} {size} {order} pizza(s).")
            print(f"Your total is: ${total_price:.2f}")
            return

main()