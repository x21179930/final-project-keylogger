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

