# Name: Sean Kelly
# Student ID: 13534113
# Date: 03/02/2025
# Description: This program records customer numbers for a week and calculates the
# highest, lowest, and average daily customer count.

# a. This creates an empty list to store the number of customers each day
daily_customers = []

# b. Loop to collect user input for a week
for i in range(1, 8):  # Loop from day 1 to 7
    while True:
        try:
            count = int(input(f"Enter the number of customers for day {i}: "))
            if count < 0:
                print("The number of customers can't be negative, try again.")
                continue  # Ask again
            daily_customers.append(count)  # Append input to list
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input detected. Please enter a valid number.")

# c (i) Calculate required statistics after collecting all data
max_cust = max(daily_customers)  # The maximum customers in a day
min_cust = min(daily_customers)  # The minimum customers in a day
avg_cust = sum(daily_customers) / len(daily_customers)  # The average number of customers

# c (ii) Output results
print("\nSummary:")
print(f"Maximum customers in a day: {max_cust}")
print(f"Minimum customers in a day: {min_cust}")
print(f"Average customers in a day: {round(avg_cust, 2)}")

