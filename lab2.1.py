def multiplication(num1, num2):
    # set the initial product to 0
    product = 0
    # convert the input numbers to integers and store them as variables
    # also save the initial values of the numbers to use in the final print statemen
    multiplicand, multiplier, start_multiplicand, start_multiplier = int(num1), int(num2), int(num1), int(num2)
    for i in range(32):
        # print the current step number
        print("Step № {}: \n".format(i+1))
        # print the current values of the multiplicand and multiplier in binary form
        print("Multiplicand: \n" + finish_string_with_zeros(bin(multiplicand)[2:]) + "\nMultiplier: \n" + finish_string_with_zeros(bin(multiplier)[2:]) + "\n")
        # Check if the least significant bit of multiplier is 1
        a = multiplier & 1
        if a == 1:
            # If it is, add multiplicand to product
            print("Summing multiplicand and product.\n")
            product += multiplicand
        # Print current product in binary format
        print("Product: \n" + finish_string_with_zeros(bin(product)[2:]) + "\n")
        # Shift multiplicand left and multiplier right
        print("Shifting multiplicand left")
        print("Shifting multiplier right")
        multiplicand <<= 1
        multiplier >>= 1
    # Print the final result in binary and decimal formats
    print("\n" + finish_string_with_zeros(bin(start_multiplicand)[2:]) + "\nx\n" + finish_string_with_zeros(bin(start_multiplier)[2:]) + "\n=\n" + finish_string_with_zeros(bin(product)[2:]) + "\n")
    print(str(start_multiplicand) + " x " + str(start_multiplier) + " = " + str(product))

def finish_string_with_zeros(val):
    count = 64 - len(val)
    head = ""
    for i in range(count):
        head += "0"
    return head + val


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
multiplication(num1, num2)