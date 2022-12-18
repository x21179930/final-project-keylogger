import tkinter as tk
from tkinter import filedialog

# create the gui window
window = tk.Tk()
window.title("Encrypted Keystroke Logger")

# create the text enter box
e1 = tk.Entry(window)
e1.grid(row=3, column=2)

# create the required buttons
start_button = tk.Button(window, text="Start Logging", command=start_logging)
start_button.grid(row=4, column=2)

stop_button = tk.Button(window, text="Stop Logging", command=stop_logging)
stop_button.grid(row=5, column=2)

# create a the search button
search_button = tk.Button(window, text="Search Logs", command=search_logs)
search_button.grid(row=6, column=2)

# create a stop button
quit_button = tk.Button(window, text="Quit", command=quit_logger)
quit_button.grid(row=7, column=2)

# start the log
def start_logging():
    # callthe start function
    keylogger.start_logging()

# stop the log
def stop_logging():
    # callthe stop function
    keylogger.stop_logging()

# search the created log files
def search_logs():
    # open the log
    file_path = filedialog.askopenfilename()
    # call the encrytion/decryption function
    encryption.decrypt_log(file_path)

# stop the app
def quit_logger():
    window.destroy()


window.mainloop()
