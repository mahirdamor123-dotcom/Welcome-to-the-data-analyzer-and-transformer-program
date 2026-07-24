def new_func():
    print("============================== DATA ANALYZER ==============================")
    print("Welcome to the data Analyzer and Transformer Program")

    data = []

    while True:
        print("\n===== MENU =====")
        print("1.Input Data")
        print("2. Display Data Summary (Built-in Function)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. EXIT")

        choice = input("Enter the number of your choice from 1-7:")

        if choice == "1":

            def input_data():
                """Accepted a 1D array from the user."""
                nonlocal data
                data = list(map(int, input("Enter data for a 1D array (seperated by spaces): ").split()))
                print("\nData has been stored successfuly!")

            input_data()

        elif choice == "2":
            def display_summary():
                """Display summary of the dataset using built-in function."""
                if len(data) == 0:
                    print("No data Presented! Please enter the data")
                    return
                print("\nData Summary:")
                print("- Total elements:", len(data))
                print("- Maximum Value:", max(data))
                print("- Minimum Value:", min(data))
                print("- Sum of all values:", sum(data))
                print("- Average Value:", round(sum(data) / len(data), 2))

            display_summary()

        elif choice == "3":
            n = int(input("enter the number: "))

            def factorial(n):
                """Calculate factorial using recursion."""
                if n == 0 or n == 1:
                    return 1
                return n * factorial(n - 1)

            print(factorial(n))

        elif choice == "4":
            def filter_data():
                """Filter values using lambda"""
                limit = int(input("enter the threshold: "))
                result = list(filter(lambda x: x >= limit, data))
                print(result)

            filter_data()

        elif choice == "5":
            def sort_data():
                """Sort the data"""
                print("1. Ascending")
                print("2. Descending")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print(sorted(data))
                elif choice == 2:
                    print(sorted(data, reverse=True))

            sort_data()

        elif choice == "6":
            def statistics():
                """Return multiple values"""
                maximum = max(data)
                minimum = min(data)
                total = sum(data)
                average = total / len(data)
                return minimum, maximum, total, average

            minimum, maximum, total, average = statistics()
            print("Minimum:", minimum)
            print("Maximum:", maximum)
            print("Total:", total)
            print("Average:", average)

        elif choice == "7":
            print("thank you for using the Data Analyzeer and Transform Program. good bye!")
            break

        else:
            print("Invalid Choice")

new_func()