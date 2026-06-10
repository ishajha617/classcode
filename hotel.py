print("===== HOTEL MANAGEMENT HIRING SYSTEM =====")

# Input
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
qualification = input("Enter Your Qualification: ")
experience = int(input("Enter Your Experience (Years): "))

# Age Verification
if age >= 18:

    print("\nWelcome", name)
    print("You are eligible to apply.\n")

    while True:

        print("\n===== HOTEL DEPARTMENTS =====")
        print("1. Cooking")
        print("2. Cleaning")
        print("3. Waiter")
        print("4. Reception")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            dish = input("Enter Your Best Dish: ")
            print("Selected Department: Cooking")

        elif choice == 2:
            cleaning_exp = input("Do you have cleaning experience (Yes/No): ")
            print("Selected Department: Cleaning")

        elif choice == 3:
            print("Selected Department: Waiter")
            print("Interview Scheduled.")

        elif choice == 4:
            print("Selected Department: Reception")
            print("Communication Skills Required.")

        elif choice == 5:
            print("Thank You For Visiting.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Sorry! Age must be 18 or above.")