bakery_shop = {"coke": 200, "muffins": 28, "cupcake": 36, "pie": 57, "pastry_pack": 20, "others": 25}

cart = {}

print("Available items:")
for item, quantity in bakery_shop.items():
    print(f"{item}: {quantity}")

while True:
    action = input("Enter 'add' to choose an item or 'remove' to delete an item, or 'checkout' to pay: ")
    if action == "add":
        item = input("Enter the name of the item you want to add: ")
        if item in bakery_shop:
            quantity = int(input("Enter the quantity you want to add: "))
            if quantity <= bakery_shop[item]:
                if item in cart:
                    cart[item] += quantity
                else:
                    cart[item] = quantity
                bakery_shop[item] -= quantity
                print(f"{quantity} {item} added to the cart.")
            else:
                print(f"Sorry, we only have {bakery_shop[item]} {item} available.")
        else:
            print("Sorry, that item is not available.")
    elif action == "remove":
        item = input("Enter the name of the item you want to remove: ")
        if item in cart:
            quantity = int(input("Enter the quantity you want to remove: "))
            if quantity <= cart[item]:
                cart[item] -= quantity
                bakery_shop[item] += quantity
                print(f"{quantity} {item} removed from the cart.")
                if cart[item] == 0:
                    del cart[item]
            else:
                print(f"Sorry, you only have {cart[item]} {item} in your cart.")
        else:
            print("Sorry, that item is not in your cart.")
    elif action == "checkout":
        total = 0
        print("Your cart contains:")
        for item, quantity in cart.items():
            price = quantity * bakery_shop[item]
            total += price
            print(f"{quantity} {item} - {price} dollars")
        print(f"Total: {total} dollars. Thank you for shopping with us!")
        break
    else:
        print("Sorry, that is not a valid action. Please try again.")