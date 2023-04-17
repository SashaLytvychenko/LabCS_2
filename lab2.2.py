import math


def division(num1, num2):
    divider = int(num1)  # convert the first parameter to an integer and assign it to "divider"
    divisor = int(num2)  # convert the second parameter to an integer and assign it to "divisor"
    register = divider  # assign "divider" to "register"
    quotient = int(math.pow(2, 32) - 1)  # calculate the maximum quotient for 32-bit integers
    remainder_length = 32  # set the bit length of the remainder to 32
    quotient_length = 32  # set the bit length of the quotient to 32
    register_length = 64  # set the bit length of the register to 64

    print("\nNumbers in binary:")
    print("Divider:\t" + finish_string_with_zeros(bin(divider)[2:], remainder_length)) # print the binary representation of the divider
    print("Divisor:\t" + finish_string_with_zeros(bin(divisor)[2:], remainder_length))

    subtract_divisor = -(divisor << 32) # shift the divisor left by 32 bits
    divisor <<= 32

    for i in range(32):
        print("\nStep №" + str(i+1))  # print the current step number
        print("Register:\t" + finish_string_with_zeros(bin(register)[2:], register_length)) # print the binary representation of the register
        register <<= 1  # shift the register left by 1 bit
        print("Зсуваємо регістр вліво на один біт;")

        if register >= divisor:
            print("Remainder більший(або рівний) ніж Divisor")

            register += subtract_divisor # subtract the divisor from the register
            register |= 1  # set the least significant bit of the register to 1
            print("Register:\t" + finish_string_with_zeros(bin(register)[2:], register_length)) # print the binary representation of the register
        else: # if the register is less than the divisor
            print("Remainder менший ніж Divisor")

            print("Register:\t" + finish_string_with_zeros(bin(register)[2:], register_length))

    print("\nAnswer:")
    print("Quotient:\t" + finish_string_with_zeros(bin(register & quotient)[2:], quotient_length) +
          " ( " + str(register & quotient) + " )")
    print("Remainder:\t" + finish_string_with_zeros(bin(register >> 32)[2:], remainder_length) +
          " ( " + str(register >> 32) + " )")

def finish_string_with_zeros(val, bitscount):
    count = bitscount - len(val)
    head = ""
    for i in range(count):
        head += "0"
    return head + val

num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")
division(num1, num2)