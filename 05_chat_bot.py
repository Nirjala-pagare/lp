def main():

    print("================================================")
    print("         WELCOME TO SMARTSHOP CHATBOT")
    print("================================================")

    name = input("Enter your name: ")

    print("\nHello", name + "!")
    print("Type 'menu' to see services.")
    print("Type 'exit' to end the chat.\n")

    while True:

        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Thank you for visiting SmartShop!")
            print("Bot: Have a great day!")
            break

        elif user == "menu":
            print("\n========= AVAILABLE SERVICES =========")
            print("1. Product Information")
            print("2. Order Status")
            print("3. Payment Methods")
            print("4. Return Policy")
            print("5. Delivery Details")
            print("6. Contact Support")
            print("7. Offers and Discounts")
            print("8. Store Timings")
            print("9. Account Help")
            print("10. Exit")
            print("======================================")

        elif user in ["hi", "hello", "hey", "good morning", "good evening"]:
            print("Bot: Hello!", name + ", how can I help you today?")

        elif user in ["how are you", "how are you?"]:
            print("Bot: I am fine and ready to help you!")

        elif user in ["product", "product information", "product details"]:
            print("Bot: We offer electronics, clothes, shoes, watches, and accessories.")

        elif user in ["mobile", "laptop", "electronics"]:
            print("Bot: Latest electronics are available with exciting discounts.")

        elif user in ["clothes", "fashion", "tshirt", "jeans"]:
            print("Bot: Trendy fashion collections are available for men and women.")

        elif user in ["price", "cost", "offer price"]:
            print("Bot: Prices vary depending on the product and ongoing offers.")

        elif user in ["discount", "offers", "sale"]:
            print("Bot: Flat 20% discount is available on selected products.")

        elif user in ["order", "track order", "order status", "where is my order"]:
            print("Bot: Your order will be delivered within 3-5 working days.")

        elif user in ["cancel order", "order cancel"]:
            print("Bot: Orders can be cancelled before shipping.")

        elif user in ["delivery", "delivery details", "shipping"]:
            print("Bot: Standard delivery takes 3-5 days.")

        elif user in ["fast delivery", "express delivery"]:
            print("Bot: Express delivery is available in selected cities.")

        elif user in ["payment", "payment methods", "payment options"]:
            print("Bot: We support UPI, Debit Card, Credit Card, Wallets, and Net Banking.")

        elif user in ["cash on delivery", "cod"]:
            print("Bot: Cash on Delivery is available on eligible products.")

        elif user in ["refund", "return", "return policy", "exchange"]:
            print("Bot: Products can be returned within 7 days of delivery.")

        elif user in ["damaged product", "wrong product"]:
            print("Bot: Sorry for the inconvenience. Please request a replacement.")

        elif user in ["support", "help", "contact support"]:
            print("Bot: Contact us at support@smartshop.com")

        elif user in ["store timing", "timing", "working hours"]:
            print("Bot: Our online support is available 24/7.")

        elif user in ["account", "login issue", "password reset"]:
            print("Bot: Please use the 'Forgot Password' option on login page.")

        elif user in ["thank you", "thanks", "thx"]:
            print("Bot: You're welcome,", name + "!")

        elif user in ["bye", "goodbye"]:
            print("Bot: Goodbye!", name)
            break

        else:
            print("Bot: Sorry, I did not understand your query.")
            print("Bot: Please type 'menu' to see available services.")


main()