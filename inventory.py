# ============================================
#                Shoe Class
# ============================================

class Shoe:
    """
    Represents a shoe item in the inventory.
    Stores country, code, product name, cost, and quantity.
    """

    def __init__(self, country, code, product, cost, quantity):
        # Initialise attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """
        Return a readable string representation of the shoe.
        Useful for printing and debugging.
        """
        return (
            f"{self.country}, {self.code}, {self.product}, "
            f"{self.cost}, {self.quantity}"
        )


# ============================================
#           Shoe List (Global Store)
# ============================================

shoe_list = []


# ============================================
#           Inventory Functions
# ============================================

def read_shoes_data():
    """
    Read shoe data from inventory.txt.
    Skip the header line, create Shoe objects,
    and append them to shoe_list.
    Includes error handling for missing files.
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header

            for line in file:
                if line.strip() == "":
                    continue

                country, code, product, cost, quantity = (
                    line.strip().split(",")
                )

                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("Error: inventory.txt file not found.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def capture_shoes():
    """
    Capture shoe details from the user,
    create a Shoe object, and add it to shoe_list.
    """
    country = input("Enter country: ")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    print("Shoe added successfully.")


def view_all():
    """
    Print all shoes in the inventory.
    Uses the __str__ method of the Shoe class.
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    print("\n=== ALL SHOES ===")
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """
    Find the shoe with the lowest quantity.
    Ask the user whether to restock it.
    Update both the object and the inventory file.
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    # Find shoe with minimum quantity
    lowest = min(shoe_list, key=lambda s: s.quantity)

    print(f"Lowest stock item:\n{lowest}")

    choice = input("Would you like to restock this item? (yes/no): ").lower()

    if choice == "yes":
        add_qty = int(input("Enter quantity to add: "))
        lowest.quantity += add_qty

        print("Stock updated.")
        update_inventory_file()


def search_shoe():
    """
    Search for a shoe by its code.
    Print and return the shoe if found.
    """
    code = input("Enter shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print("Shoe found:")
            print(shoe)
            return shoe

    print("Shoe not found.")
    return None


def value_per_item():
    """
    Calculate and display the total value of each shoe item.
    Formula: value = cost * quantity
    """
    print("\n=== VALUE PER ITEM ===")

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: £{value}")


def highest_qty():
    """
    Identify the shoe with the highest quantity.
    Print it as the item 'for sale'.
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    highest = max(shoe_list, key=lambda s: s.quantity)

    print("\n*** FOR SALE ***")
    print(highest)


def update_inventory_file():
    """
    Rewrite inventory.txt with updated shoe data.
    Ensures file stays in sync with program changes.
    """
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},"
                f"{shoe.cost},{shoe.quantity}\n"
            )


# ============================================
#                 Main Menu
# ============================================

def main():
    """
    Display the main menu and route user choices
    to the appropriate functions.
    """
    read_shoes_data()

    while True:
        print(
            """
======== MENU ========
1 - View all shoes
2 - Add new shoe
3 - Restock lowest quantity
4 - Search shoe by code
5 - View value per item
6 - View highest quantity (for sale)
7 - Exit
"""
        )

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()

        elif choice == "2":
            capture_shoes()

        elif choice == "3":
            re_stock()

        elif choice == "4":
            search_shoe()

        elif choice == "5":
            value_per_item()

        elif choice == "6":
            highest_qty()

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
