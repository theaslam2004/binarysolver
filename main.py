def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def add_binary(binary1, binary2):
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    sum_decimal = decimal1 + decimal2
    return decimal_to_binary(sum_decimal)

def main():
    print("Binary Number Solver")
    print("====================")
    while True:
        print("\nMenu:")
        print("1. Convert binary to decimal")
        print("2. Convert decimal to binary")
        print("3. Add two binary numbers")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            binary = input("Enter a binary number: ")
            print("Decimal equivalent:", binary_to_decimal(binary))
        elif choice == '2':
            decimal = int(input("Enter a decimal number: "))
            print("Binary equivalent:", decimal_to_binary(decimal))
        elif choice == '3':
            binary1 = input("Enter first binary number: ")
            binary2 = input("Enter second binary number: ")
            print("Sum of binary numbers:", add_binary(binary1, binary2))
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
