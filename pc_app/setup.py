import tkinter as tk
import subprocess
import psutil
import socket
import os

class FlaskServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Remote PC Controller")

        self.root.geometry("300x180")

        icon_path = os.path.join(os.path.dirname(__file__), 'appicon.ico')
        self.root.iconbitmap(icon_path)

        self.start_button = tk.Button(root, text="Start App", command=self.check_and_start_server)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop App", command=self.stop_server)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(root, text="App Status: Not Running")
        self.status_label.pack(pady=10)

        powered_by_label = tk.Label(root, text="Powered by Encode99", font=("Helvetica", 10))
        powered_by_label.pack(side=tk.BOTTOM)

    def is_server_running(self):
        for process in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if "python" in process.info['name'] and "app.py" in process.info['cmdline']:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())

    def check_and_start_server(self):
        if self.is_server_running():
            self.status_label.config(text=f"App Status: Running\nIP Address: {self.get_ip_address()}")
        else:
            self.start_server()
            self.status_label.config(text=f"App Status: Running\nIP Address: {self.get_ip_address()}")

    def start_server(self):
        self.status_label.config(text="App Status: Running")
        self.server_process = subprocess.Popen(["pythonw", "_internal/app.py"])
        # self.server_process = subprocess.Popen(["python", "app.py"])

    def stop_server(self):
        if hasattr(self, 'server_process') and self.server_process.poll() is None:
            self.terminate_process_tree(self.server_process.pid)
            self.server_process.wait()
            self.status_label.config(text="Server Status: Not Running")

    def terminate_process_tree(self, pid):
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.terminate()
        parent.terminate()


if __name__ == "__main__":
    root = tk.Tk()
    app = FlaskServerApp(root)
    root.mainloop()
