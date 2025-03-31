import socket
from encryption import decrypt_message, encrypt_message
from conversion import (
    infix_to_postfix, postfix_to_infix, prefix_to_postfix,
    prefix_to_infix, postfix_to_prefix, infix_to_prefix
)


# Function to handle client request
def handle_client(conn):
    encrypted_message = conn.recv(1024).decode()  # Receive encrypted message
    message = decrypt_message(encrypted_message)  # Decrypt message

    # Split into expression and conversion type
    expression, conversion_type = message.split('|')

    # Perform the requested conversion
    if conversion_type == 'infix_to_postfix':
        result = infix_to_postfix(expression)
    elif conversion_type == 'postfix_to_infix':
        result = postfix_to_infix(expression)
    elif conversion_type == 'prefix_to_postfix':
        result = prefix_to_postfix(expression)
    elif conversion_type == 'prefix_to_infix':
        result = prefix_to_infix(expression)
    elif conversion_type == 'postfix_to_prefix':
        result = postfix_to_prefix(expression)
    elif conversion_type == 'infix_to_prefix':
        result = infix_to_prefix(expression)
    else:
        result = "Invalid conversion type"

    # Encrypt result and send to client
    encrypted_result = encrypt_message(result)
    conn.send(encrypted_result.encode())


# Start the server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5001))
    server.listen(5)

    print("Server is running on port 5000...")

    while True:
        conn, addr = server.accept()
        print(f"Connected to {addr}")
        handle_client(conn)
        conn.close()


if __name__ == "__main__":
    main()
