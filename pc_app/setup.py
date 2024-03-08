import tkinter as tk
import subprocess
import psutil
import socket
import os
import webbrowser

class FlaskServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Remote PC Controller")

        self.root.geometry("400x250")

        icon_path = os.path.join(os.path.dirname(__file__), 'appicon.ico')
        self.root.iconbitmap(icon_path)

        self.start_button = tk.Button(root, text="Start App", command=self.check_and_start_server)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop App", command=self.stop_server)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(root, text="App Status: Not Running")
        self.status_label.pack(pady=10)

        self.server_text_widget = tk.Label(root, text="Open Server Home page", fg="blue", cursor="hand2")
        self.server_text_widget.pack(pady=10)
        self.server_text_widget.bind("<Button-1>", self.open_server_link)

        self.help_text_widget = tk.Label(root, text="Help and Documentation", fg="blue", cursor="hand2")
        self.help_text_widget.pack(pady=10)
        self.help_text_widget.bind("<Button-1>", self.open_help_link)

        self.powered_by_label = tk.Label(root, text="Powered by Encode99", font=("Helvetica", 10))
        self.powered_by_label.pack(side=tk.BOTTOM)

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
            ip_address = self.get_ip_address()
            self.status_label.config(text=f"App Status: Running\nIP Address: {ip_address}")

            # Create a clickable link to open the browser to the server's home page
            link_text = f"Open Server Home Page ({ip_address}:12345)"
            self.server_text_widget.config(text=link_text, fg="blue", cursor="hand2")

        else:
            self.start_server()
            ip_address = self.get_ip_address()
            self.status_label.config(text=f"App Status: Running\nIP Address: {ip_address}")

    def start_server(self):
        self.status_label.config(text="App Status: Running")
        self.server_process = subprocess.Popen(["_internal/bin/app.exe"])
        # self.server_process = subprocess.Popen(["bin/app.exe"])

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

    def open_server_link(self, event):
        ip_address = self.get_ip_address()
        webbrowser.open(f"http://{ip_address}:12345")

    def open_help_link(self, event):
        webbrowser.open("https://dilumsadeepa.github.io/Remote-PC-Controller/help")


if __name__ == "__main__":
    root = tk.Tk()
    app = FlaskServerApp(root)
    root.mainloop()
