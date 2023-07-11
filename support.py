import sqlite3
from cryptography.fernet import Fernet
import os
import time
import datetime
import pytz
# import telebot


# Database uasge

def encrypt_text(plaintext, pw):
    cipher = Fernet(pw.encode('ascii'))

    return cipher.encrypt(plaintext)


def decrypt_text(ciphertext, pw):
    cipher = Fernet(pw.encode('ascii'))

    return cipher.encrypt(ciphertext)
    

def decrypt_dbase():
    cipher = Fernet(os.environ.get('db_pw').encode('ascii'))
    
    with open('encrypted.bin', 'rb') as file:
        ciphertext = file.read()
    

    with open('database.db', 'wb') as file:
        file.write(cipher.decrypt(ciphertext))


def encrypt_dbase():
    cipher = Fernet(os.environ.get('db_pw').encode('ascii'))
    
    with open('database.db', 'rb') as file:
        plaintext = file.read()

    with open('encrypted.bin', 'wb') as file:
        file.write(cipher.encrypt(plaintext))

    os.remove('database.db')
    

def dbase_write(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    
    id = cursor.lastrowid
    conn.commit()
    conn.close()
    return id


def db_write(username, password):
    path = 'encrypted.bin'
    
    if not os.path.exists(path):
        id = dbase_write(username, password)
        encrypt_dbase()
            
    else :
        decrypt_dbase()
        id = dbase_write(username, password)
        encrypt_dbase()

    return id


# Logger for telegram bot
 
def logUser(log, reply, message):
    log.write(f"{message.id} | [{time.ctime(message.date)}] | User : {message.text}\n")


def logBot(log, reply, message):
    log.write(f"{message.id + 1} | [{time.ctime(time.time())}] | Bot : {reply}\n")


def fileLog(reply, message):
    logPath = f"log_{message.from_user.id}.txt"
    if not os.path.exists(logPath):
        with open(logPath, 'a') as log:
            log.write(f'''User Id : {message.from_user.id}
User Name : {message.from_user.username}
First Name : {message.from_user.first_name}
Last Name : {message.from_user.last_name}
Bot : {message.from_user.is_bot}\n\n\n\n''')
    with open(logPath, 'a') as log:
        logUser(log, reply, message)
        logBot(log, reply, message)


def print_request(request):
    print("Received Request:")
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.get_data()}")


def login_verify(username, password):
    # pass

    decrypt_dbase()
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    encrypt_dbase()

    return result[0]
    
    """
    # if username and password not in database:
    #     say the password and database does not exist. Do you want to sign up?

    if username and password is in database:
        say welcome back
        
    elif username is in database but password is not:
        say worng password
    
    elif username not in database:
        say wrong username
    """


# Decorator for showing local time

def local_time():
    timezone = pytz.timezone('Asia/Kolkata')
    formatted_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time)
    return None
