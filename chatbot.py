# ==========================================================
# LP-II MINI PROJECT
# ELEMENTARY CUSTOMER SUPPORT CHATBOT
# Includes Sorting Algorithms:
# 1. Bubble Sort
# 2. Selection Sort
# 3. Insertion Sort
# ==========================================================

# ---------------- PRODUCT DATA ----------------

products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1200},
    {"name": "Headphones", "price": 2000},
    {"name": "Mobile", "price": 25000}
]

orders = [
    {"order_id": 101, "amount": 4500},
    {"order_id": 102, "amount": 1200},
    {"order_id": 103, "amount": 9000},
    {"order_id": 104, "amount": 2500}
]

tickets = [
    {"ticket_id": 1, "issue": "Payment failed", "priority": 2},
    {"ticket_id": 2, "issue": "Order not delivered", "priority": 1},
    {"ticket_id": 3, "issue": "Return request", "priority": 3},
    {"ticket_id": 4, "issue": "Login problem", "priority": 2}
]


# ---------------- SORTING ALGORITHMS ----------------

def bubble_sort_products_by_price(products):
    n = len(products)

    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j]["price"] > products[j + 1]["price"]:
                products[j], products[j + 1] = products[j + 1], products[j]

    return products


def selection_sort_orders_by_amount(orders):
    n = len(orders)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if orders[j]["amount"] < orders[min_index]["amount"]:
                min_index = j

        orders[i], orders[min_index] = orders[min_index], orders[i]

    return orders


def insertion_sort_tickets_by_priority(tickets):
    n = len(tickets)

    for i in range(1, n):
        key = tickets[i]
        j = i - 1

        while j >= 0 and tickets[j]["priority"] > key["priority"]:
            tickets[j + 1] = tickets[j]
            j -= 1

        tickets[j + 1] = key

    return tickets


# ---------------- DISPLAY FUNCTIONS ----------------

def show_products():
    print("\nAvailable Products:")
    for product in products:
        print(product["name"], "- Rs.", product["price"])


def show_sorted_products():
    sorted_products = bubble_sort_products_by_price(products.copy())

    print("\nProducts Sorted by Price using Bubble Sort:")
    for product in sorted_products:
        print(product["name"], "- Rs.", product["price"])


def show_sorted_orders():
    sorted_orders = selection_sort_orders_by_amount(orders.copy())

    print("\nOrders Sorted by Amount using Selection Sort:")
    for order in sorted_orders:
        print("Order ID:", order["order_id"], "- Amount: Rs.", order["amount"])


def show_sorted_tickets():
    sorted_tickets = insertion_sort_tickets_by_priority(tickets.copy())

    print("\nSupport Tickets Sorted by Priority using Insertion Sort:")
    print("Priority 1 = High, Priority 2 = Medium, Priority 3 = Low")

    for ticket in sorted_tickets:
        print("Ticket ID:", ticket["ticket_id"],
              "| Issue:", ticket["issue"],
              "| Priority:", ticket["priority"])


def show_faq():
    print("\nFrequently Asked Questions:")
    print("1. Delivery usually takes 3 to 5 working days.")
    print("2. Return policy is valid for 7 days after delivery.")
    print("3. Refund is processed within 5 to 7 working days.")
    print("4. You can contact customer care at support@example.com.")


# ---------------- CHATBOT ----------------

def chatbot():
    print("==========================================")
    print(" Welcome to SmartShop Customer Chatbot")
    print("==========================================")

    name = input("Enter your name: ")
    print("\nHello", name + "!", "How can I help you today?")

    while True:
        print("\n-------------- MENU --------------")
        print("1. View available products")
        print("2. Sort products by price")
        print("3. Sort orders by amount")
        print("4. Sort support tickets by priority")
        print("5. View FAQs")
        print("6. Exit")
        print("----------------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_products()

        elif choice == 2:
            show_sorted_products()

        elif choice == 3:
            show_sorted_orders()

        elif choice == 4:
            show_sorted_tickets()

        elif choice == 5:
            show_faq()

        elif choice == 6:
            print("\nThank you for using SmartShop Chatbot.")
            print("Have a nice day!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ---------------- MAIN PROGRAM ----------------

chatbot()