print("1. You must enter at least 3 numbers.")
print("2. All numbers must be positive (> 0).")
print("3. Separate the numbers using spaces.")
print(" ")

inting_list = []

while len(inting_list) < 3:

    entered_nums = input("Enter the numpers here: ")
    listing_nums = entered_nums.split()
    inting_list = []

    for i in listing_nums:

        inted_i = int(i)
        inting_list.append(inted_i)

    # for i in inting_list:
    #     if i <= 0:
    #         print("Number either 0 or negative: Try again: ")
    #         continue

    if len(inting_list) < 3:

        print("Not enough numbers. Try again: ")

print(" ")
print("1 Enter a new series (replace the old one)")
print("2 Show the series in the order you entered it")
print("3 Show the series in reverse order")
print("4 Show the series sorted from smallest to largest")
print("5 Display the largest number (Max)")
print("6 Display the smallest number (Min)")
print("7 Calculate and display the average value")
print("8 Display how many numbers are in the series")
print("9 Calculate and display the sum of all numbers")
print("0 Exit the program")