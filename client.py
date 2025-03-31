import socket
from encryption import encrypt_message, decrypt_message


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5001))

    # Get input from user
    expression = input("Enter expression: ")
    print("\nConversion Types:")
    print("1. infix_to_postfix")
    print("2. postfix_to_infix")
    print("3. prefix_to_postfix")
    print("4. prefix_to_infix")
    print("5. postfix_to_prefix")
    print("6. infix_to_prefix")

    conversion_type = input("Enter conversion type: ")

    # Encrypt message and send
    encrypted_message = encrypt_message(expression + '|' + conversion_type)
    client.send(encrypted_message.encode())

    # Receive encrypted response and decrypt
    encrypted_response = client.recv(1024).decode()
    response = decrypt_message(encrypted_response)

    print(f"\nResult: {response}")

    client.close()


if __name__ == "__main__":
    main()
