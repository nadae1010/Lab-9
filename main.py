def encode_password(password):
    # Check if the password is 8 digits long
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password must be 8 digits long and contain only integers.")

    # Initialize an empty string to store the encoded password
    encoded_password = ""

    # Iterate through each digit in the password
    for digit in password:
        # Shift the digit up by 3 numbers
        # To handle the wrap-around when adding 3, we use modulus 10
        encoded_digit = (int(digit) + 3) % 10
        # Convert the encoded digit back to a string and add to the encoded_password
        encoded_password += str(encoded_digit)

    return encoded_password


def decode_password(encoded_password):
    encoded_password_list = []
    for digit in encoded_password:
        encoded_password_list += digit
    encoded_password_list = list(map(int, encoded_password_list))
    decoded_password_list = [x - 3 for x in encoded_password_list]
    decoded_password = "". join(map(str, decoded_password_list))
    return decoded_password


if __name__ == "__main__":
    # Test the encode_password function
    password = input("Enter an 8-digit password containing only integers: ")

    try:
        encoded = encode_password(password)
        print("Encoded Password:", encoded)
    except ValueError as e:
        print("Error:", e)

