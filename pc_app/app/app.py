from flask import Flask, jsonify, render_template,request
import ctypes
import pyautogui
import os
import socket
import pyperclip
import psutil
import sys



app = Flask(__name__)

sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

@app.route('/')
def index():
    # Get the running IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Application information
    app_info = {
        "name": "Remort PC Controller",
    }

    return render_template('index.html', ip_address=ip_address, app_info=app_info)

@app.route('/check')
def chechserver():
    return jsonify({"message": "yes"}), 200

@app.route('/lock')
def lock_screen():
    ctypes.windll.user32.LockWorkStation()
    return jsonify({"message": "Screen locked."}), 200

@app.route('/minmax')
def minimize_window():
    pyautogui.hotkey('win', 'd')
    return jsonify({"message": "Window minimized."}), 200

@app.route('/close')
def closeit():
    pyautogui.hotkey('Alt', 'F4')
    return jsonify({"message": "Window Closed."}), 200

@app.route('/poweroff')
def power_off():
    os.system("shutdown /s /t 1")
    return jsonify({"message": "Powering Off."}), 200

@app.route('/restart')
def restart_pc():
    os.system("shutdown /r /t 1")
    return jsonify({"message": "Restarting PC."}), 200

@app.route('/sleep')
def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return jsonify({"message": "Sleeping PC."}), 200


@app.route('/copy', methods=['POST'])
def copy_option():
    data = request.get_json()
    message = data.get('data', 'No message provided')

    # Set the clipboard content
    pyperclip.copy(message)

    return jsonify({'response': f'Successfully paste'}), 200

@app.route('/paste')
def paste_clipboard():
    clipboard_data = pyperclip.paste()
    return jsonify({'response': clipboard_data}), 200


@app.route('/winkey')
def send_win_key():
    pyautogui.press('win')
    return jsonify({"message": "Win key pressed."}), 200

@app.route('/prev')
def send_previous():
    pyautogui.press('prevtrack')
    return jsonify({"message": "Previous key pressed."}), 200

@app.route('/upa')
def send_up_arrow():
    pyautogui.press('up')
    return jsonify({"message": "Up arrow key pressed."}), 200

@app.route('/next')
def send_next():
    pyautogui.press('nexttrack')
    return jsonify({"message": "Next key pressed."}), 200

@app.route('/lefta')
def send_left_arrow():
    pyautogui.press('left')
    return jsonify({"message": "Left arrow key pressed."}), 200

@app.route('/play')
def send_play_pause():
    pyautogui.press('playpause')
    return jsonify({"message": "Play/Pause key pressed."}), 200

@app.route('/righta')
def send_right_arrow():
    pyautogui.press('right')
    return jsonify({"message": "Right arrow key pressed."}), 200

@app.route('/tabk')
def send_tab_key():
    pyautogui.press('tab')
    return jsonify({"message": "Tab key pressed."}), 200

@app.route('/downa')
def send_down_arrow():
    pyautogui.press('down')
    return jsonify({"message": "Down arrow key pressed."}), 200

@app.route('/enterk')
def send_enter_key():
    pyautogui.press('enter')
    return jsonify({"message": "Enter key pressed."}), 200

@app.route('/vd')
def send_vd_key():
    pyautogui.press('volumedown')
    return jsonify({"message": "Volume Down."}), 200

@app.route('/vm')
def send_vm_key():
    pyautogui.press('volumemute')
    return jsonify({"message": "Volume Mute."}), 200

@app.route('/vu')
def send_vu_key():
    pyautogui.press('volumeup')
    return jsonify({"message": "Volume Up."}), 200




   


    
# Add routes for other commands...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345, debug=False)
