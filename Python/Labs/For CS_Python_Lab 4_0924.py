def encrypt_data():
    # Read the input from the user
    input_data = input().strip()

    # Check if the input is a valid integer
    if not input_data.isdigit():
        print("Enter only integer value")
        return

    # Convert the input to an integer
    num = int(input_data)

    # Check for the number of digits (it should be exactly 4)
    if len(input_data) < 4:
        print("Provided input is less than 4, enter four digit integers")
        return
    elif len(input_data) > 4:
        print("Provided input is more than 4, enter four digit integers")
        return

    # Ensure the number is positive
    if num < 0:
        print("Enter positive 4-digit integer")
        return

    # Extract each digit
    digits = [int(digit) for digit in input_data]

    # Add 5 to each digit and take the remainder when divided by 10
    encrypted_digits = [(digit + 5) % 10 for digit in digits]

    # Swap the first and third digits, and the second and fourth digits
    encrypted_digits[0], encrypted_digits[2] = encrypted_digits[2], encrypted_digits[0]
    encrypted_digits[1], encrypted_digits[3] = encrypted_digits[3], encrypted_digits[1]

    # Join the encrypted digits to form the final encrypted integer
    encrypted_number = ''.join(map(str, encrypted_digits))

    # Output the encrypted integer
    print(encrypted_number)

# Call the function to encrypt data
encrypt_data()
