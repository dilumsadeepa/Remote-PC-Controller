import socket

def send_command(command):
    HOST = '127.0.0.1'  # Change to the IP address of your server
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        data = s.recv(1024)

    print('Received feedback:', data.decode())

# Example usage
send_command('lock')
