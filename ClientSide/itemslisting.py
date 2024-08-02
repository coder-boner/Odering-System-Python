import socket
import os

#importing item lists from imported files
from meats import meatitems
from dairy import dairyitems

items = meatitems + '\n' + dairyitems

print(items)

#ordering items
from ordering import orderinput

#test for sending message to server ip
ORDER_ID_FILE = 'last_order_id.txt'

def get_next_order_id():
    if os.path.exists(ORDER_ID_FILE):
        with open(ORDER_ID_FILE, 'r') as file:
            last_order_id = int(file.read())
    else:
        last_order_id = 0

    next_order_id = last_order_id + 1

    with open(ORDER_ID_FILE, 'w') as file:
        file.write(str(next_order_id))

    return next_order_id

def send_message(order_id, message, server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (server_ip, 65432)
    client_socket.connect(server_address)
    
    try:
        full_message = f"{order_id}:{message}"
        client_socket.sendall(full_message.encode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_ip = '127.0.0.1'  # Change this to the server's IP address
    order_id = get_next_order_id()
    message = orderinput
    send_message(order_id, message, server_ip)
