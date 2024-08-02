import socket
import os

LOG_DIR = 'logs'
LOG_LIMIT = 100

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def get_log_file():
    files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith('orders_')])
    if files:
        latest_file = files[-1]
        with open(os.path.join(LOG_DIR, latest_file), 'r') as file:
            lines = file.readlines()
            if len(lines) < LOG_LIMIT:
                return latest_file
    return f'orders_{len(files) + 1}.txt'

def log_order(order_id, message):
    ensure_log_dir()
    log_file = get_log_file()
    with open(os.path.join(LOG_DIR, log_file), 'a') as file:
        file.write(f'{order_id}:{message}\n')



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 65432)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print('Waiting for a connection...')
    
    while True:
        connection, client_address = server_socket.accept()
        try:
            print(f'Connection from {client_address}')
            
            while True:
                data = connection.recv(1024)
                if data:
                    decoded_data = data.decode()
                    print(f'Received: {decoded_data}')
                    parts = decoded_data.split(':')
                    if len(parts) == 2:
                        order_id, message = parts
                        if message == '1':
                            message = '500g BEEF MINCE'
                        print(f'Order ID: {order_id}, Message: {message}')
                        log_order(order_id, message)
                else:
                    break
        finally:
            connection.close()

if __name__ == "__main__":
    start_server()
