# Shopping Cart Program in Python

def  SheinShoppingCart:
    def __init__(self):
        self.shoes = []
        self.prices = []  
        self.discounts = []  

    def add_shoe(self):
        shoe_name = input("Enter your shoe name: ")
        brand = input("Enter brand: ")
        size = input("Enter size: ")
        price = float(input("Enter price: "))
        self.shoes.append({"shoe": shoe_name, "brand": brand, "size": size})
        self.prices.append(price)
        print(f"Added {shoe_name} to cart ")

    def calculate_discount(self):
        self.discounts = []  # Reset discounts list
        for price in self.prices:
            if price > 500:
                discount = price * 0.05
            else:
                discount = 0
            self.discounts.append(discount)

    def display_cart(self):
        print("-- Your Cart --")
        for shoe in self.shoes:
            print(f"Shoe: {shoe['shoe']}, Brand: {shoe['brand']}, Size: {shoe['size']}")
        for i in range(len(self.prices)):
            print(f"Price: R{self.prices[i]}, Discount: R{self.discounts[i]}")
        self.calculate_total()

    def calculate_total(self):
        total = sum(self.prices) - sum(self.discounts)
        shipping = 50
        total += shipping
        print(f"Shipping cost: R{shipping}")
        print(f"Total: R{total}")

def main():
    cart = ShoppingCart()
    while True:
        print("\nShopping Cart Menu:")
        print("1. Enter your shoe")
        print("2. Display Cart")
        print("3. Checkout (Exit)")
        choice = input("Enter choice: ")
        
        if choice == "1":
            cart.add_shoe()
        elif choice == "2":
            cart.calculate_discount()
            cart.display_cart()
        elif choice == "3":
            print("Thanks for shopping! ")
            break
        else:
            print("Invalid choice, try again ")

if __name__ == "__main__":
    main()
    