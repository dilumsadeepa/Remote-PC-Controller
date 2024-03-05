import socket
import threading
import ctypes
import pyautogui
import os
import time

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345       # Choose a port number

def lock_screen():
    print("Locking screen...")
    ctypes.windll.user32.LockWorkStation()
    print("Screen locked.")
    return "Screen locked."

def minimize_window():
    print("Minimizing window...")
    pyautogui.hotkey('win', 'd')
    return "Window minimized."

def maximize_window():
    pyautogui.hotkey('win', 'd')
    return "Window maximized."

def power_off():
    os.system("shutdown /s /t 1")
    return "Powering off."

def restart_pc():
    os.system("shutdown /r /t 1")
    return "Restarting PC."

def sleep_pc():
    print("Sleeping")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return "PC in sleep mode."

def handle_command(conn, addr):
    print('Connected by', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        command = data.decode()  # Extract the command from the received data
        print('Received command:', command)

        feedback =""

        if command == '001':
            break
        elif command == 'lock':
            feedback = lock_screen()
        elif command == 'minimize':
            feedback = minimize_window()
        elif command == 'maximize':
            feedback = maximize_window()
        elif command == 'sleep':
            feedback = sleep_pc()
        elif command == 'poweroff':
            feedback = power_off()
        elif command == 'restart':
            feedback = restart_pc()

        # Send feedback to the client
        print(feedback)
        conn.sendall(feedback.encode())

    print('Client', addr, 'disconnected')
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print("Server started. Listening for commands...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_command, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
